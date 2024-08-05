---
permalink: /cv
layout: single
toc: true
toc_label: "On this page"
toc_sticky: true
toc_icon: "list-ul"
title: "CV"
# classes: wide
toc_icon: "columns"
---

# Professional Impact

Dr. Jonathan Trueblood is a software developer at Metaspectral, a
Vancouver-based startup leveraging hyperspectral imaging (HSI) technology. With a PhD
in Atmospheric and Physical Chemistry and a decade of environmental science
research, he brings a unique blend of scientific rigor and software craftsmanship to his work.

Jonathan currently develops Metaspectral's Fusion Platform, a
cloud-based platform for processing HSI data and training deep learning models.
He is the project lead for the development of the Fusion Platform's FusionAI
feature, which integrates AI into the system for user interaction, analytical insights, and workflow automation. 

As an environmental information expert Hatfield Consultants (2021-2023) he enhanced
EnviroData, a C#-based web application for environmental data management, by
designing, building, and maintaining various microservices, integrating
R-based workflows and leading its migration to the Azure Cloud Platform. 

Jonathan's multi-faceted expertise in experimental science, software development, and cross-disciplinary communication allows him to tackle complex and challenging problems. He has conducted research in labs worldwide, including France and New Zealand. His fieldwork has taken him to remote locations, such as the coasts of New Zealand and the Southern Ocean. These unique experiences have provided him with exceptional problem-solving skills and a deep understanding of how to innovate and adapt in diverse environments.

# Professional Experience

## Software Engineer, [Metaspectral](https://metaspectral.com/)
*2023 - present*  
Backend developer of Fusion Platform, a cloud-based application for hyperspectral image (HSI) processing and deep learning model training.  

**Key Technologies**:
- **Backend**: Python, FastAPI, Celery, RabbitMQ, Redis
- **Database**: MySQL, SQLAlchemy, MongoDB
- **Frontend**: React, Typescript, TanStack, Recoil
- **DevOps and Infrastructure**:  Google Cloud Platform, Google Kubernetes
  Engine, Vertex AI, Docker, Vault, Locust, Prometheus, Grafana, Jenkins
- **External APIs**: OpenAI Assistants API
 
**Responsibilities and Projects**:  
- **FusionAI**  
  - Conceptualized and developed **FusionAI**, an AI assistant for the Fusion
    platform, aimed at augmenting user support and automating tasks with
    AI-driven capabilities.  
  - **Core Features**:
    - **Automated Guidance System**: Implemented a system to offer automated, interactive guidance for dataset analysis and deep learning model training, facilitating an AI-enhanced learning and development process for users.
    - **Image Heuristics Automation**: Developed a feature that automatically generates image heuristics by programming an interface with the Fusion platform API. This interface initiates Celery tasks that run chemometric models in Docker containers, analyzing image metadata to produce customized insights.
    - **Contextual User Support**: Created a user support framework using document
      embeddings, enabling the provision of in-depth, relevant assistance based on
      the user's current context and needs.
  - **Architecture and Design**:  
    - **Compatibility and Integration**: Architected and integrated FusionAI's core features, ensuring seamless compatibility with Fusion's pre-existing infrastructure.
    - **Large Language Model (LLM) Integration**: Integrated OpenAI's Assistants API to power the FusionAI service. Designed the integration with flexibility in mind, allowing for the seamless substitution or addition of alternative APIs and LLM providers, including proprietary models, as required.
    - **Innovative Message Processing System**: Combined traditional programming techniques with modern large language model design patterns to establish an advanced message processing system. This system accurately translates user queries into defined objectives, tasks, and subtasks, which are then executed by LLM agents, simplifying complex operations on the Fusion platform.
    - **RAG Pipelines and Predictive Task Launching**: Adopted Retrieval-Augmented Generation (RAG) pipelines and forward-looking task execution strategies, effectively reducing response times and operational costs. These innovations were crucial in creating a user experience of immediate AI responsiveness, despite the inherent processing delays of complex LLMs.

- **Fusion Platform Development**
  - Implemented the CI/CD pipeline, co-leading with a focus on Continuous
    Deployment (CD) by establishing a secure and systematic flow of configuration,
    environment variables and secrets management via Vault in a GKE cluster.
  - Built a load-testing suite with Locust, ensuring the Fusion platform maintains high performance and reliability standards under varying loads.
  - Built and maintained a full-fledged monitoring solution on GKE, leveraging PromTail, Prometheus, and Grafana to deliver critical insights for continuous system optimization.


## Environmental Information Specialist, [Hatfield Environmental Consultants](https://hatfieldgroup.com)
*2021 - 2023*  
Led the development of Hatfield’s web-based data management and 
analytics application, EnviroData. Maintained EnviroData’s various
microservices.  Provided analytical and technical support for various projects.
Developed R-based tools for analytical and statistical analysis.

**Key Technologies**:
- **Backend**: R, C#/.NET, MySQL, microservices
- **Cloud Infrastructure**: Microsoft Azure, Azure Kubernetes Service, Argo Workflows
- **DevOps**: Continuous Integration and Deployment Pipelines, Docker
- **Project**: Management: Agile Methodologies, Scrum

**Responsibilities and Projects**:  
  - **EnviroData Developer**  
    - Develop R-based microservices that integrated into the service registry
      written in .NET
    - Served as product owner and scrum master, leading bi-weekly sprint planning and review meetings.
    - Conducted system administration and maintenance, user onboarding, training, and support, while developing user documentation.
    - Cloud Migration: Planned and executed the migration of the EnviroData application from local servers to Microsoft Azure, enhancing scalability and reliability.
    - DevOps Pipeline: Built an automated DevOps pipeline for continuous integration and deployment, facilitating seamless updates to Azure virtual machines.
    - Documentation: Developed and maintained comprehensive documentation for EnviroDataR, an R-based client for API data management and analysis.
- **Data Management Support, Global Container Terminal, British Columbia**  
  - Collaborated with Hatfield staff, field scientists, and lab technicians to manage environmental data from various monitoring surveys and sampling programs.
  - Designed and developed EcoSurveys feature, a service that streamlines the handling and storage of diverse ecological data types.
  - Advanced Query Service: Designed the EcoSurvey Report Query Service to enable advanced querying capabilities for EcoSurvey data. 
  

- **Permitting and Report Support, Various Projects**  
  - Executed data compilation, wrangling, and analysis, creating detailed tables and figures for reports.
  - Developed and maintained R-based tools and packages for comprehensive analysis tasks.
  - **Specific Contributions**:
    - **Endako Mine, British Columbia, Centerra Gold**: Produced the Aquatic Effects Monitoring Programs Report, Annual Water Quality Report, and Continuous Improvement Framework for 2021.
    - **Silvertip Mine, British Columbia, Coeur Mining Inc**: Compiled the Annual Monitoring Report and Annual Reclamation Report for Water Quality Monitoring in 2021.
    - **Kemess Mine, British Columbia, Centerra Gold**: Completed the Annual Water Quality Report for 2021.
    - **Copper Mountain Mine, British Columbia, Copper Mountain Mining Corporation**: Developed the Annual Monitoring Report for Water Quality in 2021.
  
- **Data Management and Site Support, Silvertip Mine, British Columbia**  
  - Managed client data via EnviroData, overseeing data transfers from lab technicians.
  - Created R scripts to streamline administrative tasks and enhance data management efficiency.

# Education
*2019 - 2021*  
**Postdoc**, Centre National de la Recherche Scientifique  
*Supervisor:* Dr. Karine Sellegri  
*Topic:* Modeling ocean biological production of atmospheric ice nucleating particles  


*2013 - 2018*  
**PhD in Atmospheric and Physical Chemistry**, UC San Diego  
[Center for Aerosol Impacts on Chemistry of the Environment](https://caice.ucsd.edu/)  
*Supervisor:* Prof. Vicki H. Grassian  
*Topic:* Spectroscopic investigations into nascent and aged sea spray aerosol  


*2011 - 2013*  
**MS in Atmospheric Science**, North Carolina State University  
*Supervisor:* Prof. Nicholas Meskhidze  
*Topic:* Formation mechanisms of volatile organic compounds over remote marine regions  


*June - August 2010*  
**Undergraduate Research Assistant in Machine Learning**, University of Oklahoma  
*Supervisor:* Prof. Amy McGovern  
*Topic:* Predicting convectively induced turbulence using spatiotemporal random relational forests  

*June - August 2008 and 2009*  
**Undergraduate Research Assistant in Atmospheric Science**, Dordt University  
*Supervisor:* Prof. Doug Allen  
*Topic:* Analysis and modeling of the stratosphere above the polar arctic region

*2007 - 2011*  
**BA in Physics**, Dordt University  

# Publications

**Trueblood, J. V.**;  Nicosia, A.;  Engel, A.;  Zäncker, B.;  Rinaldi, M.;  Freney, E.;  Thyssen, M.;  Obernosterer, I.;  Dinasquet, J.;  Belosi, F.;  Tovar-Sánchez, A.;  Rodriguez-Romero, A.;  Santachiara, G.;  Guieu, C.; Sellegri, K., A Two-Component Parameterization of Marine Ice Nucleating Particles Based on Seawater Biology and Sea Spray Aerosol Measurements in the Mediterranean Sea. *Atmos. Chem. Phys.* **2021**, *21*, 4659–4676.

Freney, E.;  Sellegri, K.;  Nicosia, A.;  **Trueblood, J. V.**;  Bloss, M.;  Rinaldi, M.;  Prevot, A.;  Slowik, J. G.;  Thyssen, M.;  Gregori, G.;  Engel, A.;  Zancker, B.;  Desboeufs, K.;  Asmi, E.;  Lefevre, D.; Guieu, C., Mediterranean Nascent Sea Spray Organic Aerosol and Relationships with Seawater Biogeochemistry. *Atmos. Chem. Phys. Discuss.* **Manuscript Accepted, 2021**.

**Trueblood, J. V.**;  Wang, X.;  Or, V. W.;  Alves, M. R.;  Santander, M. V.;  Prather, K. A.; Grassian, V. H., The Old and the New: Aging of Sea Spray Aerosol and Formation of Secondary Marine Aerosol through OH Oxidation Reactions. *ACS Earth and Space Chemistry* **2019**, *3* (10), 2307-2314.

**Trueblood, J. V.**;  Alves, M. R.;  Power, D.;  Santander, M. V.;  Cochran, R. E.;  Prather, K. A.; Grassian, V. H., Shedding Light on Photosensitized Reactions within Marine-Relevant Organic Thin Films. *ACS Earth and Space Chemistry* **2019**, *3* (8), 1614-1623.

DeMott, P. J.;  Mason, R. H.;  McCluskey, C. S.;  Hill, T. C. J.;  Perkins, R. J.;  Desyaterik, Y.;  Bertram, A. K.;  **Trueblood, J. V.**;  Grassian, V. H.;  Qiu, Y.;  Molinero, V.;  Tobo, Y.;  Sultana, C. M.;  Lee, C.; Prather, K. A., Ice nucleation by particles containing long-chain fatty acids of relevance to freezing by sea spray aerosols. *Environmental Science: Processes & Impacts* **2018**, *20* (11), 1559-1569.

McCluskey, C. S.;  Hill, T. C. J.;  Sultana, C. M.;  Laksina, O.;  **Trueblood, J. V.**;  Santander, M. V.;  Beall, C. M.;  Michaud, J. M.;  Kreidenweis, S. M.;  Prather, K. A.;  Grassian, V. H.; DeMott, P. J., A Mesocosm Double Feature: Insights into the Chemical Makeup of Marine Ice Nucleating Particles. *J. Atmos. Sci.* **2018**, *75*, 2405-2423.

Cochran, R. E.;  Laskina, O.;  **Trueblood, J. V.**;  Estillore, A. D.;  Morris, H. S.;  Jayarathne, T.;  Sultana, C. M.;  Lee, C.;  Lin, P.;  Laskin, J.;  Laskin, A.;  Dowling, J. A.;  Qin, Z.;  Cappa, C. D.;  Bertram, T. H.;  Tivanski, A. V.;  Stone, E. A.;  Prather, K. A.; Grassian, V. H., Molecular Diversity of Sea Spray Aerosol Particles: Impact of Ocean Biology on Particle Composition and Hygroscopicity. *Chem* **2017**, *2* (5), 655-667.

Estillore, A. D.;  **Trueblood, J. V.**; Grassian, V. H., Atmospheric chemistry of bioaerosols: heterogeneous and multiphase reactions with atmospheric oxidants and other trace gases. *Chemical Science* **2016**, *7* (11), 6604-6616.

Chen, T.-H.;  Wang, L.; **Trueblood, J. V.**;  Grassian, V. H.; Cohen, S. M., Poly(isophthalic acid)(ethylene oxide) as a Macromolecular Modulator for Metal–Organic Polyhedra. *Journal of the American Chemical Society* **2016**, *138* (30), 9646-9654.

**Trueblood, J. V.**;  Estillore, A. D.;  Lee, C.;  Dowling, J. A.;  Prather, K. A.; Grassian, V. H., Heterogeneous Chemistry of Lipopolysaccharides with Gas-Phase Nitric Acid: Reactive Sites and Reaction Pathways. *The Journal of Physical Chemistry A* **2016**, *120* (32), 6444-6450.

Wang, X.;  Sultana, C. M.;  **Trueblood, J.**;  Hill, T. C. J.;  Malfatti, F.;  Lee, C.;  Laskina, O.;  Moore, K. A.;  Beall, C. M.;  McCluskey, C. S.;  Cornwell, G. C.;  Zhou, Y.;  Cox, J. L.;  Pendergraft, M. A.;  Santander, M. V.;  Bertram, T. H.;  Cappa, C. D.;  Azam, F.;  DeMott, P. J.;  Grassian, V. H.; Prather, K. A., Microbial Control of Sea Spray Aerosol Composition: A Tale of Two Blooms. *ACS Central Science* **2015**, *1* (3), 124-131.

Ault, A. P.;  Guasco, T. L.;  Baltrusaitis, J.;  Ryder, O. S.;  **Trueblood, J. V.**;  Collins, D. B.;  Ruppel, M. J.;  Cuadra-Rodriguez, L. A.;  Prather, K. A.; Grassian, V. H., Heterogeneous Reactivity of Nitric Acid with Nascent Sea Spray Aerosol: Large Differences Observed between and within Individual Particles. *The Journal of Physical Chemistry Letters* **2014**, *5* (15), 2493-2500.

Allen, D. R.;  Douglass, A. R.;  Manney, G. L.;  Strahan, S. E.;  Krosschell, J. C.;  **Trueblood, J. V.**;  Nielsen, J. E.;  Pawson, S.; Zhu, Z., Modeling the Frozen-In Anticyclone in the 2005 Arctic Summer Stratosphere. *Atmos. Chem. Phys.* **2011**, *11* (9), 4557-4576.



# Community Service and Leadership Positions  

**Instructor**, Clubes de Ciencia, Monterrey, Mexico, August 2018  
*Developed and taught a week-long course on sea sprsay aerosols, climate, and ocean biogeochemistry to high school students in Mexico.*



**Student Leadership Committee**, [Center for Aerosol Impacts on Chemistry of the Environment](https://caice.ucsd.edu/), UC San Diego, 2016 - 2018  
*Maintained interface between CAICE students and PI's through bi-weekly meetings. Planned and led weekly student meetings.*



**Department of Chemistry Open House Presenter**, University of Iowa, September 2015  
*Planned and held demonstrations during UIowa Department of Chemistry open houses.*



**Presenter**, [California State Summer School for Mathematics and Science (COSMOS)](https://jacobsschool.ucsd.edu/cosmos/), UC San Diego, September 2015  
*Planned and taught laboratory experiment sessions with students geared towards the radiatived properties of atmospheric green house gases.*



**Presenter**, [Iowa Climate Festival](https://www.icgov.org/ic-climate-fest), University of Iowa, April 2014 and April 2015  
*Planned and conducted demonstrations for the community to raise awareness of climate science at the annual Iowa Climate Festival.*
 

# Awards

*2017*
Runner-up UCSD GRADSlam Competition 


*2016 - 2017*
San Diego Fellowship 


*2015*
Center for Global and Regional Environmental Research Graduate Student Travel Award


*2011*
Honorable Mention Presentation at 91st American Meteorological Society Annual Meeting

*2007 - 2011*
Dordt University Presidnetial Scholarship

*2007 - 2011*
Dordt University Concert Band Scholarship

*2007 - 2011*
Dordt University Cross Country/Track Scholarship

