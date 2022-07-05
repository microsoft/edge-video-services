# Sets static global variables for Jupyter notebooks

import warnings
import logging
logging.disable(logging.WARNING)

try:
    from dotenv import set_key, get_key, find_dotenv
    envPath = find_dotenv(raise_error_if_not_found=True)
except IOError:
    import os
    from pathlib import Path

    try:
        project_folder = Path(__file__).parent.absolute()
        envPath = find_dotenv(os.path.join(project_folder, '.env'))
    except Exception:
        print(".env not found")

azureSubscriptionId = get_key(envPath, "SUBSCRIPTION_ID")
resourceLocation = get_key(envPath, "RESOURCE_LOCATION")
resourceGroupName = get_key(envPath, "RESOURCE_GROUP")
iotHubServiceName = get_key(envPath, "IOT_HUB_SERVICE_NAME")
iotDeviceId = get_key(envPath, "IOT_DEVICE_ID")
storageServiceName = get_key(envPath, "STORAGE_SERVICE_NAME")
noderesourceGroupName = get_key(envPath, "NODE_RESOURCEGROUP")
aksclustername = get_key(envPath, "AKS_CLUSTERNAME")
aksdns = get_key(envPath, "AKS_DNS")
gpuvmtype = get_key(envPath, "GPU_VM_SIZE")
videoinputfolderondevice = get_key(envPath, "VIDEO_INPUT_FOLDER_ON_DEVICE")
evsclientimage = get_key(envPath, "EVSCLIENT_IMAGE")
evsclientendpointlocal = get_key(envPath, "EVSCLIENT_ENDPOINTLOCAL")
evsclientendpointtype = get_key(envPath, "EVSCLIENT_ENDPOINTTYPE")
evsclientendpointremote = get_key(envPath, "EVSCLIENT_ENDPOINTREMOTE")
evsclientfolderondevice = get_key(envPath, "EVSCLIENT_OUTPUT_FOLDER_ON_DEVICE")
evsclientlin = get_key(envPath, "EVSCLIENT_LINE")
evsclientvideourl = get_key(envPath, "EVSCLIENT_VIDEOURL")
evsclientsamplingrate = get_key(envPath, "EVSCLIENT_SAMPLINGRATE")
evsclientcategory = get_key(envPath, "EVSCLIENT_CATEGORY")
rocketoutputfolderondevice = get_key(envPath, "ROCKET_OUTPUT_FOLDER_ON_DEVICE")
rocketimage = get_key(envPath, "ROCKET_IMAGE")
rocketpipeline = get_key(envPath, "ROCKET_PIPELINE")
rocketline = get_key(envPath, "ROCKET_LINE")