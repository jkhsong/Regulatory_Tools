# Research_Tools

<br><h1>Introduction</h1>
The purpose of FDA Research Science Tools (RSTs), developed by the FDA-CDRH's Office of Science and Engineering Labs (OSEL), is to assist in the development of new medical technologies.  

Initially, <b>Research_Tools</b> analyzes the 117 RSTs offered by FDA-OSEL in three manners: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1\. The availability of RSTs by industry type. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. The availability of RSTs by tool type (i.e. Laboratory Method, etc.). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3\. How RST tool types serve various areas of research. <br>
The data for these analyses are extracted from the [Catalog of Regulatory Science Tools to Help Assess New Medical Devices](https://www.fda.gov/medical-devices/science-and-research-medical-devices/catalog-regulatory-science-tools-help-assess-new-medical-devices).
  

<p><br>Next, open-source industry data is integrated to offer three additional analyses: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Interactions between RST parameters and industry size. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Interactions between RST parameters and industry growth. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6. Interactions between RST parameters and industry employment <br> 

<h1>How the program works:</h1>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Strings cleaned, stripped, lemmatized using Python (packages such as pandas, etc.). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Areas automatically reduced to base disciplines (Neurology Oncology -> Neurology) by root words (i.e. "Neurology"). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Pushes data to PostgreSQL server to store data. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Uses SQL retrieve and form relevant tables. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Uses Python to perform higher level inferences. <br>

<br><br><h1>Sample outputs:</h1>

<b>Types of RSTs found: </b>
| Type of RSTs              |   Counts |
|:--------------------------|:--------:|
| ClinicalOutcomeAssessment |        1 |
| Dataset                   |        5 |
| LabMethod                 |       68 |
| Model                     |       31 |
| ModelDataset              |        1 |
| PhantomPhysical           |       10 |
| PhantomVirtual            |        1 |

<br><br><b>Types of Area of Research found: </b>
| Area of Research                            |   #RSTs Available |
|:--------------------------------------------|:-----------------:|
| additivemanufacturing                       |                 2 |
| artificialintelligencemachinelearning       |                 4 |
| biocompatibilitytoxicology                  |                12 |
| cardiovascular                              |                23 |
| credibilityassessmentinmodeling             |                 5 |
| digitalpathology                            |                 2 |
| electromagneticelectricalsafety             |                16 |
| evaluationof3dbreastimagingsystems          |                 2 |
| materialsperformance                        |                 6 |
| medicalimagingdiagnostics                   |                25 |
| microbiologyinfectioncontrol                |                14 |
| neurology                                   |                11 |
| ophthalmology                               |                 8 |
| orthopedics                                 |                12 |
| postmarketsignalresponsematerialperformance |                 1 |
| therapeuticultrasound                       |                 7 |

<br><br><b>RST subtypes offered per Area of Research:</b>
| Area of Research                            |   ClinicalAssess            |   Dataset |   LabMethod |   Model |   ModelDataset |   PhantomPhysical |   PhantomVirtual |
|:--------------------------------------------|:---------------------------:|:---------:|:-----------:|:-------:|:--------------:|:-----------------:|:----------------:|
| additivemanufacturing                       |                           0 |         0 |           2 |       0 |              0 |                 0 |                0 |
| artificialintelligence                      |                           0 |         0 |           1 |       3 |              0 |                 0 |                0 |
| biocompatibilitytoxicology                  |                           0 |         0 |           9 |       3 |              0 |                 0 |                0 |
| cardiovascular                              |                           0 |         4 |          10 |      10 |              1 |                 0 |                0 |
| credibilitymodeling                         |                           0 |         0 |           4 |       1 |              0 |                 0 |                0 |
| digitalpathology                            |                           0 |         1 |           0 |       1 |              0 |                 0 |                0 |
| electromagneticelectricalsafety             |                           0 |         0 |          10 |       6 |              0 |                 0 |                0 |
| 3dbreastimagingsystems                      |                           0 |         0 |           0 |       0 |              0 |                 2 |                0 |
| materialsperformance                        |                           0 |         0 |           5 |       1 |              0 |                 0 |                0 |
| medicalimagingdiagnostics                   |                           0 |         1 |           5 |      12 |              0 |                 6 |                1 |
| microbiologyinfectioncontrol                |                           0 |         0 |          14 |       0 |              0 |                 0 |                0 |
| neurology                                   |                           1 |         0 |           6 |       4 |              0 |                 0 |                0 |
| ophthalmology                               |                           0 |         0 |           5 |       3 |              0 |                 0 |                0 |
| orthopedics                                 |                           1 |         0 |           5 |       6 |              0 |                 0 |                0 |
| materialperformance                         |                           0 |         0 |           1 |       0 |              0 |                 0 |                0 |
| therapeuticultrasound                       |                           0 |         0 |           4 |       1 |              0 |                 2 |                0 |

<br><br><b>K-Means Classications of Research Areas by RST subtypes:</b>
| Area of Research                            |   Category | RSTs (C,D,L,M,MD,PP,PV)   |
|:--------------------------------------------|-----------:|:--------------------------|
| additivemanufacturing                       |          0 | (0, 0, 2, 0, 0, 0, 0)     |
| artificialintelligencemachinelearning       |          0 | (0, 0, 1, 3, 0, 0, 0)     |
| credibilityassessmentinmodeling             |          0 | (0, 0, 4, 1, 0, 0, 0)     |
| digitalpathology                            |          0 | (0, 1, 0, 1, 0, 0, 0)     |
| evaluationof3dbreastimagingsystems          |          0 | (0, 0, 0, 0, 0, 2, 0)     |
| postmarketsignalresponsematerialperformance |          0 | (0, 0, 1, 0, 0, 0, 0)     |
| therapeuticultrasound                       |          0 | (0, 0, 4, 1, 0, 2, 0)     |

| Area of Research                            |   Category | RSTs (C,D,L,M,MD,PP,PV)   |
|:--------------------------------------------|:----------:|---------------------------|
| cardiovascular                              |          1 | (0, 4, 10, 10, 1, 0, 0)   |
| medicalimagingdiagnostics                   |          1 | (0, 1, 5, 12, 0, 6, 1)    |

| Area of Research                            |   Category | RSTs (C,D,L,M,MD,PP,PV)   |
|:--------------------------------------------|:----------:|---------------------------|
| microbiologyinfectioncontrol                |          2 | (0, 0, 14, 0, 0, 0, 0)    |

| Area of Research                            |   Category | RSTs (C,D,L,M,MD,PP,PV)   |
|:--------------------------------------------|:----------:|---------------------------|
| biocompatibilitytoxicology                  |          3 | (0, 0, 9, 3, 0, 0, 0)     |
| electromagneticelectricalsafety             |          3 | (0, 0, 10, 6, 0, 0, 0)    |
| materialsperformance                        |          3 | (0, 0, 5, 1, 0, 0, 0)     |
| neurology                                   |          3 | (1, 0, 6, 4, 0, 0, 0)     |
| ophthalmology                               |          3 | (0, 0, 5, 3, 0, 0, 0)     |
| orthopedics                                 |          3 | (1, 0, 5, 6, 0, 0, 0)     |