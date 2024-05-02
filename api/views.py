from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import torch
import PIL.Image as Image
from torchvision import transforms
# Create your views here.

model = torch.load('AImodel.pth', map_location=torch.device('cpu'))
print("Model Initialized!")



class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer


class DoctorDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = DoctorDetectionResults.objects.all()
    serializer_class = DoctorDetectionResultsSerialzer

class PatientDetectionResultsViewSet(viewsets.ModelViewSet):
    queryset = PatientDetectionResults.objects.all()
    serializer_class = PatientDetectionResultsSerialzer

    def perform_create(self, serializer):
        result = serializer.save()
        # image_url = serializer.data['image']
        # print(image_url)
        image_url = serializer.instance.image.path

        detection_result = self.detection(image_url)
        if detection_result[0] == 0:
            result.result = 'Normal'
        elif detection_result[0] == 1:
            result.result = 'Mild'
        elif detection_result[0] == 2:
            result.result = 'Moderate'
        elif detection_result[0] == 3:
            result.result = 'Severe'
        elif detection_result[0] == 4:
            result.result = 'Proliferative DR'

        result.save()


    def detection(self, imageUrl, *args, **kwargs):
        image = Image.open(imageUrl)
        image = image.convert('RGB')
        preprocess = transforms.Compose([transforms.Resize([512,512]),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
        image_tensor = preprocess(image)
        if len(image_tensor.shape) == 3:
            image_tensor= image_tensor.unsqueeze(0)
        model.eval()
        with torch.no_grad():
                for batch,x in enumerate(image_tensor):
                    outputs= model(image_tensor.to('cpu')) 
                    probabilities= torch.softmax(outputs,dim=1)
                    predictions = probabilities.argmax(dim=1).cpu().detach().tolist() #Predicted labels for an image batch.
        print(predictions)
        return predictions

    