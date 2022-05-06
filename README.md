# NM10k Dataset

![](./assets/images/overview-dataset.png)

**NM10k** is a new diverse real-world dataset from [Nullmax](http://nullmax.ai/), consisting **10k training images (640x384)**, **4k validation images (640x384)** and corresponding 2D bounding box annotations with 5 representative object categories (car, truck, bus, pedestrian, bicycle). The dataset also covers a diverse range of scenarios, such as different road grades (e.g. highway, expressway, city street and country road), different weathers (e.g. sunny, cloudy and rainy) and different times of day (e.g. daytime, evening and night). In addition, we also make 1k traffic cone masks, 100 traffic barrel masks, and 50 traffic warning triangle masks available to the community. 

Below is the statistics of our NM10k dataset:


![](./assets/images/stats.png)

For more details, please refer to [our paper](https://arxiv.org/pdf/2205.00376.pdf).

## Downloads
**Baidu Cloud** links are available for the downloading of training and testing data.

For each training images, we manually annotate the 2D bounding box annotations with 5 representative object catgories. In addition, the global traffic scene contexts (e.g., freespace, common objects and traffic lanes) are obtained from a multi-task deep model containing three heads: (1) one semantic segmentation head for freespace segmentation; (2) another instance segmentation head for traffic lane segmentation and (3) a detection head for common road users detection.

**Training & Testing data**

|Data Type|Training set|Testing set|
|:-:|:-:|:-:|
|Image|[Download (Extraction Code: 1w2g)](https://pan.baidu.com/s/12Jf06U_whDviTTUDbLxrcw)|[Download (Extraction Code: ivtv)](https://pan.baidu.com/s/12tbCOccTSNTid4t3VnEyMg)|
|2D label|[Download (Extraction Code: akmg)](https://pan.baidu.com/s/1Gl1Fv3XregiUT6yPm8RATg)|[Download (Extraction Code: e9sc)](https://pan.baidu.com/s/1uNIHTgNTg3Wu68w-RY77Dw)|

**Supplementary data**

|Data Type| Download link|
|:-:|:-:|
|Freespace segmentation|[Download (Extraction Code: w1ux)](https://pan.baidu.com/s/1gnT8PTsLjulyV2fHNTC5JA)|
|Lane segmentation|[Download (Extraction Code: e2pg)](https://pan.baidu.com/s/1_el9sHY1dQzd6r50MQukBA)|
|Traffic cone mask|[Download (Extraction Code: mjda)](https://pan.baidu.com/s/1KKZ5i4GXejwXbv4oOYW1AA)|
|Traffic barrel mask|[Download (Extraction Code: vs8x)](https://pan.baidu.com/s/1upaFHjAQUEnaG-Dam8360A)|
|Traffic warning triangle mask|[Download (Extraction Code: 5wqf)](https://pan.baidu.com/s/1hWU8EuRDTVXiOxIcaSLGug)|

**Devkit**

Please refer to [cocoapi](https://github.com/cocodataset/cocoapi) for evaluation. In addition, we provide a [view.py](https://github.com/nullmax-vision/nullmax-vision.github.io/blob/main/scripts/view.py) script to enable you familiar with this dataset. 

## Contact
{chengerkang, linaifan, zhangying}@nullmax.ai