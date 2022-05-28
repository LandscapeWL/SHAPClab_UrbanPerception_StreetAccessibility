# SHAPClab_UrbanPerception_StreetAccessibility
This repository documents the basic data and code an urban science research work. This work will be published in the ISPRS Journal of Photogrammetry and Remote Sensing.
We have explored a new method of relying on spatial perception of streets to assess spatial quality of urban on a large scale. An empirical study is used as an example to validate our approach. A machine learning scoring model is constructed using street images of the city area. Perceptions were scored on six dimensions: beautiful, affluent, safe, lively, depressing and boring. The six dimensional perceptions were further divided into positive and negative perceptions. The top 20% of street scenes with the highest positive perception scores were considered as high quality street spaces, and the top 20% of street scenes with the highest negative perception scores were considered as low quality street spaces. Finally, high accessibility was superimposed to identify the street spaces with the highest probability of being traversed by residents and of high (low) quality.
![UrbanPerceptionOverlay](http://m.qpic.cn/psc?/V51wK6B50SnpHF0Ql90V120XkX2YMvAu/bqQfVz5yrrGYSXMvKr.cqYG0eHFfbPKpXffJlCtmX8oz7cGTepweaP7OzW.teXoFbQSDGprayhUAisLVE69xNgJD0xhbopL.Dv3whVe0jnc!/b&bo=QAZABkAGQAYBByA!&rf=viewer_4 #pic_center)
# Information
The research is carried out under the SHAPC-lab and the lab director & the corresponding author:Jie He academic social networks page:<br>
http://faculty.hitsz.edu.cn/hejie

For more information related to the research, please follow the laboratory's WeChat Official Account:<br>
![空间人文与场所计算](http://faculty.hitsz.edu.cn/ueditor/jsp/upload/image/20211206/1638770351934059707.jpeg #pic_center)
# Requirements
- ADE20K dataset
- Depthmap software
- ArcGIS software
# Python Requirements
- Pillow
- Time
- Urllib
- TensorFlow
- Tensorboard
- Keras
- Numpy
- Matplotlib
# Usage
- Image semantic segmentation training data storage<br>
`ADE20K`<br>
- Image semantic segmentation training data pre-processing storage<br>
`ADE20K_Process`<br>
- Image semantic segmentation training data pre-processing code<br>
`make_dataset`<br>
- Image semantic segmentation training and applications<br>
`SegNet_ImageSemanticSegmentation`<br>
- Street view image download and pre-processing<br>
`Streetview_Download`<br>
- Street View image perception scoring<br>
`StreetView_Score`<br>
- Urban street accessibility processing data<br>
`Depthmap`<br>
- Urban perception and street view collection point data<br>
`GIS_file`<br># SHAPClab_UrbanPerception_StreetAccessibility
