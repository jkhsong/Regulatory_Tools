# Regulatory_Tools

<h2>Project Outline</h2>
<p><b><h3>1. Introduction</h3></b>
The purpose of FDA Regulatory Science Tools (<b>RSTs</b>), developed by the FDA-CDRH's Office of Science and Engineering Labs (<b>OSEL</b>), is to assist in the development of new medical technologies.<br><br>  

<b><h3>2. Analyses</h3></b>
Initially, <b>Regulatory_Tools</b> analyzes the 117 RSTs offered by FDA-OSEL in three manners:</h3><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. The availability of RSTs by industry type. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. The availability of RSTs by tool type (i.e. Laboratory Method, etc.). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. How RST tool types serve various areas of research. <br>

The data for these analyses are extracted from the [Catalog of Regulatory Science Tools to Help Assess New Medical Devices](https://www.fda.gov/medical-devices/science-and-research-medical-devices/catalog-regulatory-science-tools-help-assess-new-medical-devices).
  

<br>Next, open-source industry data is integrated to offer three additional analyses: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Interactions between RST parameters and industry size. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Interactions between RST parameters and industry growth. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6. Interactions between RST parameters and industry employment <br> 

<b><h3>3. How the program works:</h3></b>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Strings cleaned, stripped, lemmatized using Python (packages such as pandas, etc.). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Areas automatically reduced to base disciplines (Neurology Oncology -> Neurology) by root words (i.e. "Neurology"). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Pushes data to PostgreSQL server to store data. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Uses SQL retrieve and form relevant tables. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Uses Python to perform higher level inferences. <br><br>

<b><h3>4. Interpretations:</h3></b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Table 1</b> indicates that medical imaging and cardiovascular applications are the most served areas of research regarding RST availability, followed by other clinical disciplines, microbiology and infection control, as well as biocompatibility/toxicology.  Least-served areas were materials and manufacturing, and digital or computational tools.<br> 

<b>Table 1. Area of Research.</b>
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


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Out of 117 listings, <b>Tables 2</b> and <b>3</b> indicate that the two most common types of RSTs offered were Laboratory Methods and Computational Tools (Models), which represented 84.7% of all RST types on offer.  Interestingly, the remainder of tools such as Datasets, Phantoms, and Clinical Outcome Assessments represented just 15.3% of all RST types.<br>

<b>Table 2. Types of RSTs.</b>
| Type of RSTs              |   Counts |
|:--------------------------|:--------:|
| ClinicalOutcomeAssessment |        1 |
| Dataset                   |        5 |
| LabMethod                 |       68 |
| Model                     |       31 |
| ModelDataset              |        1 |
| PhantomPhysical           |       10 |
| PhantomVirtual            |        1 |

<b>Table 3. RST subtypes offered by Area of Research.</b>
| Area of Research               |   ClinicalAssess            |   Dataset |   LabMethod |   Model |   ModelDataset |   PhantomPhysical |   PhantomVirtual |
|:-------------------------------|:---------------------------:|:---------:|:-----------:|:-------:|:--------------:|:-----------------:|:----------------:|
| additivemanufacturing          |                           0 |         0 |           2 |       0 |              0 |                 0 |                0 |
| artificialintelligence         |                           0 |         0 |           1 |       3 |              0 |                 0 |                0 |
| biocompatibilitytoxicology     |                           0 |         0 |           9 |       3 |              0 |                 0 |                0 |
| cardiovascular                 |                           0 |         4 |          10 |      10 |              1 |                 0 |                0 |
| credibilitymodeling            |                           0 |         0 |           4 |       1 |              0 |                 0 |                0 |
| digitalpathology               |                           0 |         1 |           0 |       1 |              0 |                 0 |                0 |
| electromagneticelectricalsafety|                           0 |         0 |          10 |       6 |              0 |                 0 |                0 |
| 3dbreastimagingsystems         |                           0 |         0 |           0 |       0 |              0 |                 2 |                0 |
| materialsperformance           |                           0 |         0 |           5 |       1 |              0 |                 0 |                0 |
| medicalimagingdiagnostics      |                           0 |         1 |           5 |      12 |              0 |                 6 |                1 |
| microbiologyinfectioncontrol   |                           0 |         0 |          14 |       0 |              0 |                 0 |                0 |
| neurology                      |                           1 |         0 |           6 |       4 |              0 |                 0 |                0 |
| ophthalmology                  |                           0 |         0 |           5 |       3 |              0 |                 0 |                0 |
| orthopedics                    |                           1 |         0 |           5 |       6 |              0 |                 0 |                0 |
| materialperformance            |                           0 |         0 |           1 |       0 |              0 |                 0 |                0 |
| therapeuticultrasound          |                           0 |         0 |           4 |       1 |              0 |                 2 |                0 |


<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Table 4</b> indicates that clustering Areas of Research by each area's count and type of RST offerings indicates:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Cardiovascular and Medical Imaging (areas of research) share similar RST counts and types--This is interesting coming from an ultrasound background, in which echocardiography (a medical imaging subtype involving heart imaging) is a preeminent application.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Areas involving technologies with nascent biomedical applications (i.e. additive manufacturing) and computational research are marked by a similar count and ratio of lab-method/computational type RSTs on offer.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Areas involving biomedical materials and clinical disciplines (i.e. neurology, opthamology, orthopedics) are marked by a high number of lab methods and computational models.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Microbiology and Infection Control stands alone in that their RSTs are exclusively lab methods.<br>
<b>Table 4. K-Means Classications of Research Areas by RST vectors.</b>
| Area of Research                            |   Category | RSTs (C, D, L, M, MD, PP, PV)|
|:--------------------------------------------|-----------:|:-------------------------:|
| additivemanufacturing                       |          0 | (0, 0, 2, 0, 0, 0, 0)     |
| artificialintelligencemachinelearning       |          0 | (0, 0, 1, 3, 0, 0, 0)     |
| credibilityassessmentinmodeling             |          0 | (0, 0, 4, 1, 0, 0, 0)     |
| digitalpathology                            |          0 | (0, 1, 0, 1, 0, 0, 0)     |
| evaluationof3dbreastimagingsystems          |          0 | (0, 0, 0, 0, 0, 2, 0)     |
| postmarketsignalresponsematerialperformance |          0 | (0, 0, 1, 0, 0, 0, 0)     |
| therapeuticultrasound                       |          0 | (0, 0, 4, 1, 0, 2, 0)     |
| cardiovascular                              |          1 | (0, 4, 10, 10, 1, 0, 0)   |
| medicalimagingdiagnostics                   |          1 | (0, 1, 5, 12, 0, 6, 1)    |
| microbiologyinfectioncontrol                |          2 | (0, 0, 14, 0, 0, 0, 0)    |
| biocompatibilitytoxicology                  |          3 | (0, 0, 9, 3, 0, 0, 0)     |
| electromagneticelectricalsafety             |          3 | (0, 0, 10, 6, 0, 0, 0)    |
| materialsperformance                        |          3 | (0, 0, 5, 1, 0, 0, 0)     |
| neurology                                   |          3 | (1, 0, 6, 4, 0, 0, 0)     |
| ophthalmology                               |          3 | (0, 0, 5, 3, 0, 0, 0)     |
| orthopedics                                 |          3 | (1, 0, 5, 6, 0, 0, 0)     |

<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next, RSTs were normalized by total RSTs per research area. Previously, we saw that new or more emergent areas of biomedical research (digital pathology, additive manufcaturing, AI and machine learning) had fewer available RSTs.  I hypothesized that normalizing RST vectors by total RST count would reduce the effect that research area <i>age</i> may have on classifcation. Interestingly, <b>Table 5</b> indicates that significant differences in classification with <b>Table 4</b> are achieved via normalization, however:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. We see that computational predominantly remain together in category 3, indicating that RSTs developed for these areas of research have largely been of similar types.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Similar RST types are offered for materials research, biocompatibility, and microbiology/infection control (which was previously in a category of its own). <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. "Evaluation of 3D Breast Imaging Systems" now resides in its own category, due to its exclusive reliance on Physical Phantoms as RST type.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Interestingly, all of the clinical research areas (opthalmology, neurology, cardiovascular, orthopedics) clustered together according to normalized RST types.  This suggests that the type of RST offerings are largely similar for these areas of research, which is understandable--A computational model is largely accompanied by laboratory assays.  What may be counter-intuitive are discipline such as microbiology/infection control residing outside this regime of classical testing schemes.<br>


<b>Table 5. K-Means Classications of Research Areas by <i>normalized</i> RST vectors.</b>
| Area of Research                            |   Category | RSTs (C, D, L, M, MD, PP, PV)           |
|:--------------------------------------------|:----------:|:---------------------------------------:|
| additivemanufacturing                       |          0 | (0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)     |
| biocompatibilitytoxicology                  |          0 | (0.0, 0.0, 0.75, 0.25, 0.0, 0.0, 0.0)   |
| credibilityassessmentinmodeling             |          0 | (0.0, 0.0, 0.8, 0.2, 0.0, 0.0, 0.0)     |
| materialsperformance                        |          0 | (0.0, 0.0, 0.83, 0.17, 0.0, 0.0, 0.0)   |
| microbiologyinfectioncontrol                |          0 | (0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)     |
| postmarketsignalresponsematerialperformance |          0 | (0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)     |
| cardiovascular                              |          1 | (0.0, 0.16, 0.4, 0.4, 0.04, 0.0, 0.0)   |
| electromagneticelectricalsafety             |          1 | (0.0, 0.0, 0.62, 0.38, 0.0, 0.0, 0.0)   |
| neurology                                   |          1 | (0.09, 0.0, 0.55, 0.36, 0.0, 0.0, 0.0)  |
| ophthalmology                               |          1 | (0.0, 0.0, 0.62, 0.38, 0.0, 0.0, 0.0)   |
| orthopedics                                 |          1 | (0.08, 0.0, 0.42, 0.5, 0.0, 0.0, 0.0)   |
| therapeuticultrasound                       |          1 | (0.0, 0.0, 0.57, 0.14, 0.0, 0.29, 0.0)  |
| evaluationof3dbreastimagingsystems          |          2 | (0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)     |
| artificialintelligencemachinelearning       |          3 | (0.0, 0.0, 0.25, 0.75, 0.0, 0.0, 0.0)   |
| digitalpathology                            |          3 | (0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0)     |
| medicalimagingdiagnostics                   |          3 | (0.0, 0.04, 0.2, 0.48, 0.0, 0.24, 0.04) |


<b><h3>5. Conclusion</h3></b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is worth noting that RSTs are organically developed on circumstance and needs, and cluster analysis is predominantly used to classify items with similar attributes (i.e. classifying fish type by length, width, and weight).<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;However, in our case, cluster analysis can indicate what future RST types may be for less-served areas of research. An example of this is "Evaluation of 3D imaging systems": <br>We can imagine that such a discipline would benefit from additional models, datasets, and lab methods, much like its nearest neighbors "Therapeutic Ultrasound".<br>
