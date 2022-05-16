#  EVS Configuration and Cross-Edge Adaptation

In order for video analytics pipeline to adapt to network and compute fluctuations, EVS client container can be configured _during runtime_ as to how and where data (*e.g.,* encoded frame buffer) will be sent from one edge to another. For instance, we may want a more aggressive compression of the encoded frame buffer when the bandwidth between the on-prem edge and the network edge drops. A more extreme case would be to reroute the traffic from the on-prem edge to a different network edge when the current one becomes unreachable or oversubscribed. 

To reconfigure EVS client, simply call the following REST APIs using the command below from a node in the same network. Note that the reconfiguration can also be triggered _automatically_ when EVS client subscribes to local service APIs (*e.g.,* Prometheus) or Network APIs provided operators. 

```sh
curl --location --request POST 'http://<IP>:8888/api/Config?<Key>=<Value>'
```

|Key|Default Value|Type/Range|Description|
|--|--|--|--|
|bufferSizeFrame|20|int|Size of the frame buffer to be encoded on the on-prem edge. |
|encoder|libx264|[FFmpeg video encoder](https://ffmpeg.org/ffmpeg-codecs.html#Video-Encoders)|Frame buffer encoder. |
|encodeFps|7|int|Frame buffer encoding FPS. |
|encodeCrf|30|0-51|[Constant Rate Factor](https://trac.ffmpeg.org/wiki/Encode/H.264) to set the quality/size tradeoff. |
|endpointLocal|http://rocket:7788/api/ImageItems|URI|URI of the local video ML module. |
|endpointRemote|http://evslabXXX.westus2.cloudapp.azure.com:8888/api/Video|URI|URI of the remote EVS Client module (*e.g.,* on the network edge). |
|endpointType|rocket|rocket \| triton \| openvino|Type of the video ML module connects to the local EVS Client.|
