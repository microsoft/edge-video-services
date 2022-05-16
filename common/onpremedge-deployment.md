# Deploy Edge Modules to the On-prem Edge (IoT Edge Device)
We follow the method described in [Deploy Azure IoT Edge modules from Visual Studio Code](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-deploy-modules-vscode) to deploy EVS and Rocket (pipeline #5) containers as IoT Edge Modules on on-prem edge. We have included an EVS-specific [deployment template](../templates/deployment.evs.template.json) in the current repository. 

(6.1) Copy the **.env** file created in the setup step above from **common** to the **templates** folder. This file contains properties that Visual Studio Code uses to deploy modules to an edge device.

(6.2) Right click on **templates/deployment.evs.template.json** and select **“Generate Iot Edge deployment manifest”**. This will create an IoT Edge deployment manifest file in **templates/config** folder named deployment.evs.amd64.json.

(6.3) Right click on **templates/config/deployment.evs.amd64.json** and select **"Create Deployment for single device"** and select the name of your edge device. This will trigger the deployment of the IoT Edge modules to your Edge device. 
> ❗**Note:** * Enter your Iot hub connection string - if popup comes in visual studio - You can get the string from .env file.

(6.4) View the status of the deployment in the Azure IoT Hub extension (expand 'Devices' and then 'Modules' under your IoT Edge device). EVS client container will automatically start processing the video in a couple seconds. 

### Please return to [README.md](../README.md#6-deploy-edge-modules-to-the-on-prem-edge-iot-edge-device) and follow Section 7.1 to monitor output. 