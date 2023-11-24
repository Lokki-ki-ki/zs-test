# Backend
压缩包里包含了一个flask和一个scraper的module，flask里暂时用的是dummy data; scraper主要做的事情是从一个叫SeekingAlpha的网站爬取各个公司的股东大会演讲稿。

运行flask进入backend `python run.py`即可。

# Frontend
前端是一个看板，分为三个页面，分别可以展示爬取的报告数量，各个公司的报告内容，以及各个公司的财务数据图。

运行vue进入frontend folder `npm install` 再 `npm run dev`即可。
