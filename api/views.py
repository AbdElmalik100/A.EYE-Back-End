from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import torch
import PIL.Image as Image
from torchvision import transforms
from .filters import *
# Create your views here.


model = torch.load('DR_Detection.pth', map_location=torch.device('cpu'))
print("Model Initialized!")




class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialzer

class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer
    filterset_class = PatientsFilter
    search_fields = ['full_name']

class DoctorDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetectionResults.objects.all()
    serializer_class = DoctorDetectionResultsSerialzer
    filterset_class = DoctorDetectionResultsFilter

    def perform_create(self, serializer):
        result = serializer.save()
        # image_url = serializer.data['image']
        # print(image_url)
        image_url = serializer.instance.image.path
        
        detection_result = self.detection(image_url)

        result.result_class = detection_result[0]
        
        if detection_result[0] == 0:
            result.result = 'Normal'
            result.description = 'You are at very low risk of developing any vision problems in the next 12 months. You should attend your next screening appointment in 12 months. This means no signs of retinopathy were found.'
            result.points = "There is no chances of your sight getting worse._There is no any of the four stages of Diabetic Retinopathy symptoms._No need to take any treatment, as you are in normal stage."
        elif detection_result[0] == 1:
            result.result = 'Mild'
            result.description = 'The first stage is also called background retinopathy. This means that tiny bulges (microaneurysms) have appeared in the blood vessels in the back of your eyes (retina), which may leak small amounts of blood. This is very common in people with diabetes.'
            result.points = "Your sight is not affected, although you're at a higher risk of developing vision problems in the future._You do not need treatment, but you'll need to take care to prevent the problem getting worse – read more about preventing diabetic retinopathy._The chances of your sight getting worse are higher if both of your eyes are affected."
        elif detection_result[0] == 2:
            result.result = 'Moderate'
            result.description = 'The second stage is also called pre-proliferative retinopathy. At this stage, the blood vessels in your retinas swell. They may not carry blood as well as they used to. These things can cause physical changes to the retina. This means that more severe and widespread changes are seen in the retina, including bleeding into the retina.'
            result.points = "There's a high risk that your vision could eventually be affected._You'll usually be advised to have more frequent screening appointments every 3, 6, 9 or 12 months to monitor your eyes."
        elif detection_result[0] == 3:
            result.result = 'Severe'
            result.description = 'This means that new blood vessels and scar tissue have formed on your retina, which can cause significant bleeding and lead to retinal detachment, where the retina pulls away from the back of the eye.'
            result.points = "There's a very high risk you could lose your vision._Treatment will be offered to stabilise your vision as much as possible, although it will not be possible to restore any vision you've lost"
        elif detection_result[0] == 4:
            result.result = 'Proliferative DR'
            result.description = 'In this advanced stage, new blood vessels grow in your retinas and into the gel-like fluid that fills your eyes. This growth is called neovascularization. These vessels are thin and weak. They often bleed. The bleeding can cause scar tissue.'
            result.points = "There's a high risk that your vision could eventually be affected._You may be advised to have more frequent specialised testing to monitor your eyes._You may be referred to a hospital specialist to discuss treatments that can help stop the problem getting worse."

        result.save()

    def detection(self, imageUrl, *args, **kwargs):
        image = Image.open(imageUrl)
        image = image.convert('RGB')
        preprocess = transforms.Compose([transforms.Resize([512, 512]),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
                                            transforms.RandomRotation(30)])
        image_tensor = preprocess(image)
        if len(image_tensor.shape) == 3:
            image_tensor= image_tensor.unsqueeze(0)
        model.eval()
        with torch.no_grad():
            for batch,x in enumerate(image_tensor):
                outputs= model(image_tensor.to('cpu')) 
                probabilities= torch.softmax(outputs,dim=1)
                predictions = probabilities.argmax(dim=1).cpu().detach().tolist() #Predicted labels for an image batch.
        return predictions


class PatientDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = PatientDetectionResults.objects.all()
    serializer_class = PatientDetectionResultsSerialzer
    filterset_class = PatientDetectionResultsFilter


    def perform_create(self, serializer):
        result = serializer.save()
        # image_url = serializer.data['image']
        # print(image_url)
        image_url = serializer.instance.image.path
        
        detection_result = self.detection(image_url)

        result.result_class = detection_result[0]
        
        if detection_result[0] == 0:
            result.result = 'Normal'
            result.description = 'You are at very low risk of developing any vision problems in the next 12 months. You should attend your next screening appointment in 12 months. This means no signs of retinopathy were found.'
            result.points = "There is no chances of your sight getting worse._There is no any of the four stages of Diabetic Retinopathy symptoms._No need to take any treatment, as you are in normal stage."
        elif detection_result[0] == 1:
            result.result = 'Mild'
            result.description = 'The first stage is also called background retinopathy. This means that tiny bulges (microaneurysms) have appeared in the blood vessels in the back of your eyes (retina), which may leak small amounts of blood. This is very common in people with diabetes.'
            result.points = "Your sight is not affected, although you're at a higher risk of developing vision problems in the future._You do not need treatment, but you'll need to take care to prevent the problem getting worse – read more about preventing diabetic retinopathy._The chances of your sight getting worse are higher if both of your eyes are affected."
        elif detection_result[0] == 2:
            result.result = 'Moderate'
            result.description = 'The second stage is also called pre-proliferative retinopathy. At this stage, the blood vessels in your retinas swell. They may not carry blood as well as they used to. These things can cause physical changes to the retina. This means that more severe and widespread changes are seen in the retina, including bleeding into the retina.'
            result.points = "There's a high risk that your vision could eventually be affected._You'll usually be advised to have more frequent screening appointments every 3, 6, 9 or 12 months to monitor your eyes."
        elif detection_result[0] == 3:
            result.result = 'Severe'
            result.description = 'This means that new blood vessels and scar tissue have formed on your retina, which can cause significant bleeding and lead to retinal detachment, where the retina pulls away from the back of the eye.'
            result.points = "There's a very high risk you could lose your vision._Treatment will be offered to stabilise your vision as much as possible, although it will not be possible to restore any vision you've lost"
        elif detection_result[0] == 4:
            result.result = 'Proliferative DR'
            result.description = 'In this advanced stage, new blood vessels grow in your retinas and into the gel-like fluid that fills your eyes. This growth is called neovascularization. These vessels are thin and weak. They often bleed. The bleeding can cause scar tissue.'
            result.points = "There's a high risk that your vision could eventually be affected._You may be advised to have more frequent specialised testing to monitor your eyes._You may be referred to a hospital specialist to discuss treatments that can help stop the problem getting worse."

        result.save()


    def detection(self, imageUrl, *args, **kwargs):
        image = Image.open(imageUrl)
        image = image.convert('RGB')
        preprocess = transforms.Compose([transforms.Resize([512,512]),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
                                            transforms.RandomRotation(30)])
        image_tensor = preprocess(image)
        if len(image_tensor.shape) == 3:
            image_tensor= image_tensor.unsqueeze(0)
        model.eval()
        with torch.no_grad():
            for batch,x in enumerate(image_tensor):
                outputs = model(image_tensor.to('cpu')) 
                probabilities = torch.softmax(outputs,dim=1)
                predictions = probabilities.argmax(dim=1).cpu().detach().tolist() #Predicted labels for an image batch.
        return predictions
