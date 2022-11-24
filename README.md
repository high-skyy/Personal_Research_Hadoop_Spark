<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Personal Research</h3>

  <p align="center">
    Efficient join method for big-data using Hadoop & Spark
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#idea">Idea</a></li>
    <li><a href="#progress">Progress</a></li>
  </ol>
</details>


<!-- ROADMAP -->
## Roadmap

- Research of Hadoop
- Installation of Hadoop in virtual Environment
- Implementation of existing methods in virtual environment
- Implementation of new method in virtual environment
- Implementation of new method using cloud resources (if possible)
- Testing efficiency
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MY METHOD -->
## My Method

### Idea
When joining spatial data (intersects, within ...) the original methods supported by Spark are not adequate. For example shuffle hash join or shuffle-merge join. By classifying the spatial data into many sets that have a specific value, shuffle hash join or shuffle-merge join could be applicable. After joining the spatial data the amount of data will shrink. The shrinked data then could be loaded to the main memory and be selected using orginal functions for spatial joins.

### Implementation Steps
1. Divide the space where the spatial data resides and give the divided space a specific value.
2. Make a new column for the specific value of space.
3. Join the tables using the shuffle hash join or shuffle-merge join.
4. Load intermediate results to the main memory and select the records that satisfy the condition.

<!-- PROGRESS -->
## Progress

### Study of Basic Knowledge During Progress
- Learned_basics (Directory : Learned_basics)
  - Network
  - OS

### Study of Frameworks
- Hadoop
<details>
  <summary>Details</summary>
  
- Hadoop brief information (Hadoop_brief.md)
  - Modes (Stand alone, Pseudo-distributed, Fully-distributed)
  - Hadoop Cluster concept & Cluster Architecture
- Hadoop commands (Hadoop_command.md)
- Hadoop Streaming (Hadoop_Streaming.md)
- About HDFS (HDFS.md)
  - Data flow
  - Read flow
  - Architecture
  - How it works
- Configuration (Install_setting_configuration_details.md)
  - Network
  - core-site.xml, hdfs-site.xml, yarn-site.xml
- MR (MR.md)
- Yarn (Yarn.md)
  - Resource Manager
  - Scheduler
  - Application Manager
  - Node Manager
- Temp (Temporary file for clarification) (Temp.md)
  
</details>

- ZooKeeper

<details>
  <summary>Details</summary>
  
- Configuration (Configuration.md)
- Brief information & feature (Explanation.md)
- Failover (Failover.md)
  - QJM
  - ZKFailover Controller process
  
</details>

- Spark

<details>
  <summary>Details</summary>
  
- Configuration (Configuration.md)
- Join methods (Join methods.md)
  - Broadcast Hash Join
  - Shuffle hash join
  - Shuffle sort-merge join
  - Broadcast nested loop join
- Driver & Executer (Driver & Executer.md)
- Spark API Frequently Used (Spark_API_Frequently_Used.md)
- Spark command (Spark command.md)
- Spark information (spark_information_concept.md)
  - Architecture
  - Cluster manager
  - RDD
  
</details>

- Modules

<details>
  <summary>Details</summary>
  
- Pandas (geopandas/geopandas functions.md & Pandas Functions/Pandas Function.md)
- Pyspark_modules (Spark SQL/Core class.md, Spark Session.md, temp.md)
- Pyspark test_files (test_pyspark)
  
</details>

### Troubleshooting

- Error_Handling.md

### My Environment
- Host OS : Windows 10 Pro
- RAM : 16.0 (GB)
- Virtual machine : VirtualBox
- Guest OS : centOS7
- Hadoop
- Zookeeper
- Spark
- jdk

### Installation of Hadoop(Pseudo-distributed mode)
> Complete

### Installation of Hadoop(Fully-distributed mode in virtual environment)
> Complete

### Simple test using join methods currently used in Spark
> Complete

### Implementation of new join method
> Currently in progress

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
