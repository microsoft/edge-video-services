## Configure VM as IoT Edge device

> <span style="color:green; font-weight:bold"> [!IMPORTANT] </span>  
> In case you don't have virtual machine you can create it using CLI,Portal,API ETC [Create Azure Virtual Machine](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-cli#create-virtual-machine)



#### Tested Specification 

| PC | Operating System     | Resources                        |
| :-------- | :------- | :-------------------------------- |
| `Azure Virtual Machine`      | `Ubuntu 20.04` | 16 GB RAM - 4 vCPUS |

## Install Docker Engine 
SSH into your virtual machine (IOT Edge device ) and install Docker engine by running the code snippets bellow. You can learn more about [Docker engine](https://docs.docker.com/engine/install/ubuntu/) here.

```shell
sudo apt-get -y update

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt-get -y update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```
Install the `curl` command line tool on your Iot Edge device's terminal.

```shell
sudo apt-get -y install curl
```


## Install the Azure IoT Edge Runtime
In order to run the commands below in the terminal window, be sure to update the URL with the appropriate OS for your IoT Edge device:  

```
Example:
https://packages.microsoft.com/config/ubuntu/<YOUR_OS_VERSION>/multiarch/prod.list
```

Commands to install the IoT Edge Runtime:

```shell
curl https://packages.microsoft.com/config/ubuntu/18.04/multiarch/prod.list > ./microsoft-prod.list

sudo cp ./microsoft-prod.list /etc/apt/sources.list.d/

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg

sudo cp ./microsoft.gpg /etc/apt/trusted.gpg.d/

sudo apt-get -y update

sudo apt-get -y install iotedge
```

## Configure the IoT Edge Runtime Service
You need to configure the IoT Edge Runtime service, so it will connect to the IoT Hub service in the Cloud. To do so, you need IoT Edge Device connection string, which looks like something:  

```
HostName=mkov01iothub.azure-devices.net;DeviceId=mkov01iotdevid;SharedAccessKey=QK+TiYdf1WJQJf5..........oczt1S634yI=  
```  

Now continue running the following shell commands by replacing the placeholder <IOT_EDGE_DEVICE_CONN_STRING_FROM_.ENV_FILE> in the below commands with the IoT Edge Device connection string value mentioned above.

```shell
IOT_EDGE_DEVICE_CONN_STRING="<IOT_EDGE_DEVICE_CONN_STRING_FROM_.ENV_FILE>"

configFile=/etc/iotedge/config.yaml

sudo sed -i "s#\(device_connection_string: \).*#\1\'$IOT_EDGE_DEVICE_CONN_STRING\'#g" $configFile

sudo systemctl restart iotedge
```  

## Setup Local folders on the Edge Device
Create three folders on the "IoT Edge Device", the device where we want to deploy our solution.

First folder, name it "input", will contain a sample video file that the video analytics pipeline will consume. EVS client container has its own decoder and is able to ingest both mp4 video files as well as live RTSP streams. 

Second folder, name it "evsclient", will be used to store outputs from EVS client container (*i.e.,* encoded video clips sent to the network edge). 

Third folder, name it "rocket", will be used to store outputs from Rocket video ML container (*i.e.,* intermediate inference results such as frames jpeg files from motion detection).

All folders must have read/write access for all users. Below are the commands that we use to create them and set their access permissions. Run the below commands **on the IoT Edge Device**

```
sudo mkdir -p /evs/input
sudo mkdir /evs/evsclient
sudo mkdir /evs/rocket
```

Now download the "[sample.mp4](https://aka.ms/evs-videosample)" video file into "evs/input"  
```
sudo wget https://aka.ms/evs-videosample -O /evs/input/sample.mp4
```

Finally we set these folder's access permissions.  
```
sudo chmod 777 -R /evs
```

when you list the folder contents, it should have read/write access to all as sample below:  

```

iotdev@cameraedge:~$ ls -la /evs/input/
total 25416
drwxrwxrwx 2 root root     4096 Oct 20 20:40 .
drwxrwxrwx 6 root root     4096 Oct 21 19:56 ..
-rwxrwxrwx 1 root root 26015112 Jun 24  2020 sample.mp4
```

## Restart the machine
Run the following command in the terminal window to the IoT Edge device:

```shell
sudo reboot
```