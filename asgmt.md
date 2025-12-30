# 2. Database Description
<table>
  <thead>
    <tr>
      <th style="border-top: 1px solid #000000ff; border-bottom: 1px solid #000000ff;">Feature</th>
      <th style="border-top: 1px solid #000000ff; border-bottom: 1px solid #000000ff;">Type</th>
      <th style="border-top: 1px solid #000000ff; border-bottom: 1px solid #000000ff;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>Int64</td>
      <td>Airbnb’s unique identifier for the listing.</td>
    </tr>
    <tr>
      <td>listing_url</td>
      <td>String</td>
      <td>Public Airbnb URL for the listing.</td>
    </tr>
    <tr>
      <td>scrape_id</td>
      <td>Int64</td>
      <td>Identifier of the Inside Airbnb data extraction run in which the listing was collected.</td>
    </tr>
    <tr>
      <td>last_scraped</td>
      <td>String</td>
      <td>UTC date and time when the listing was last scraped from Airbnb.</td>
    </tr>
    <tr>
      <td>source</td>
      <td>String</td>
      <td>Indicates whether the listing was discovered via neighbourhood search or from a previous scrape.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Title of the Airbnb listing.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>Detailed textual description provided by the host.</td>
    </tr>
    <tr>
      <td>neighborhood_overview</td>
      <td>String</td>
      <td>Host’s description of the surrounding neighbourhood.</td>
    </tr>
    <tr>
      <td>picture_url</td>
      <td>String</td>
      <td>URL of the Airbnb-hosted main image for the listing.</td>
    </tr>
    <tr>
      <td>host_id</td>
      <td>Int64</td>
      <td>Airbnb’s unique identifier for the host.</td>
    </tr>
    <tr>
      <td>host_url</td>
      <td>String</td>
      <td>Public Airbnb profile URL of the host.</td>
    </tr>
    <tr>
      <td>host_name</td>
      <td>String</td>
      <td>Name of the host, usually first name(s) only.</td>
    </tr>
    <tr>
      <td>host_since</td>
      <td>String</td>
      <td>Date when the host registered on Airbnb.</td>
    </tr>
    <tr>
      <td>host_location</td>
      <td>String</td>
      <td>Host’s self-reported location.</td>
    </tr>
    <tr>
      <td>host_about</td>
      <td>String</td>
      <td>Free-text biography written by the host.</td>
    </tr>
    <tr>
      <td>host_response_time</td>
      <td>String</td>
      <td>Typical time taken by the host to respond to guest messages.</td>
    </tr>
    <tr>
      <td>host_response_rate</td>
      <td>String</td>
      <td>Percentage of guest messages the host responded to within Airbnb’s response window.</td>
    </tr>
    <tr>
      <td>host_acceptance_rate</td>
      <td>String</td>
      <td>Percentage of booking requests accepted by the host.</td>
    </tr>
    <tr>
      <td>host_is_superhost</td>
      <td>String</td>
      <td>Indicates whether the host has Superhost status.</td>
    </tr>
    <tr>
      <td>host_thumbnail_url</td>
      <td>String</td>
      <td>URL of the host’s profile thumbnail image.</td>
    </tr>
    <tr>
      <td>host_picture_url</td>
      <td>String</td>
      <td>URL of the host’s full-size profile image.</td>
    </tr>
    <tr>
      <td>host_neighbourhood</td>
      <td>String</td>
      <td>Neighbourhood where the host is located, as self-reported.</td>
    </tr>
    <tr>
      <td>host_listings_count</td>
      <td>Float64</td>
      <td>Number of listings owned by the host (per Airbnb’s internal calculation).</td>
    </tr>
    <tr>
      <td>host_total_listings_count</td>
      <td>Float64</td>
      <td>Total number of listings the host has had historically.</td>
    </tr>
    <tr>
      <td>host_verifications</td>
      <td>String</td>
      <td>List of verification methods completed by the host.</td>
    </tr>
    <tr>
      <td>host_has_profile_pic</td>
      <td>String</td>
      <td>Indicates whether the host has uploaded a profile picture.</td>
    </tr>
    <tr>
      <td>host_identity_verified</td>
      <td>String</td>
      <td>Indicates whether Airbnb has verified the host’s identity.</td>
    </tr>
    <tr>
      <td>neighbourhood</td>
      <td>String</td>
      <td>Neighbourhood name as entered by the host.</td>
    </tr>
    <tr>
      <td>neighbourhood_cleansed</td>
      <td>String</td>
      <td>Standardized neighbourhood derived from latitude and longitude using public shapefiles.</td>
    </tr>
    <tr>
      <td>neighbourhood_group_cleansed</td>
      <td>Float64</td>
      <td>Higher-level geographic grouping derived from spatial data; may be missing for some cities.</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>Float64</td>
      <td>Latitude of the listing using the WGS84 coordinate system.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float64</td>
      <td>Longitude of the listing using the WGS84 coordinate system.</td>
    </tr>
    <tr>
      <td>property_type</td>
      <td>String</td>
      <td>Self-reported property type of the listing.</td>
    </tr>
    <tr>
      <td>room_type</td>
      <td>String</td>
      <td>Type of space offered (Entire place, Private room, Shared room, or Hotel).</td>
    </tr>
    <tr>
      <td>accommodates</td>
      <td>Int64</td>
      <td>Maximum number of guests the listing can.</td>
    </tr>
    <tr>
      <td>bathrooms</td>
      <td>Float64</td>
      <td>Number of bathrooms available in the listing.</td>
    </tr>
    <tr>
      <td>bathrooms_text</td>
      <td>String</td>
      <td>Textual description of bathroom arrangement, reflecting Airbnb UI format.</td>
    </tr>
    <tr>
      <td>bedrooms</td>
      <td>Float64</td>
      <td>Number of bedrooms in the listing.</td>
    </tr>
    <tr>
      <td>beds</td>
      <td>Float64</td>
      <td>Number of beds available in the listing.</td>
    </tr>
    <tr>
      <td>amenities</td>
      <td>String</td>
      <td>List of amenities provided with the listing.</td>
    </tr>
    <tr>
      <td>price</td>
      <td>String</td>
      <td>Nightly price of the listing in local currency; stored as text with currency symbol.</td>
    </tr>
    <tr>
      <td>minimum_nights</td>
      <td>Int64</td>
      <td>Minimum number of nights required per booking.</td>
    </tr>
    <tr>
      <td>maximum_nights</td>
      <td>Int64</td>
      <td>Maximum number of nights allowed per booking.</td>
    </tr>
    <tr>
      <td>minimum_minimum_nights</td>
      <td>Float64</td>
      <td>Smallest minimum-night requirement observed over the next 365 days.</td>
    </tr>
    <tr>
      <td>maximum_minimum_nights</td>
      <td>Float64</td>
      <td>Largest minimum-night requirement observed over the next 365 days.</td>
    </tr>
    <tr>
      <td>minimum_maximum_nights</td>
      <td>Float64</td>
      <td>Smallest maximum-night limit observed over the next 365 days.</td>
    </tr>
    <tr>
      <td>maximum_maximum_nights</td>
      <td>Float64</td>
      <td>Largest maximum-night limit observed over the next 365 days.</td>
    </tr>
    <tr>
      <td>minimum_nights_avg_ntm</td>
      <td>Float64</td>
      <td>Average minimum-night requirement over the next 12 months.</td>
    </tr>
    <tr>
      <td>maximum_nights_avg_ntm</td>
      <td>Float64</td>
      <td>Average maximum-night requirement over the next 12 months.</td>
    </tr>
    <tr>
      <td>calendar_updated</td>
      <td>Float64</td>
      <td>Relative indicator of how recently the listing’s calendar was</td>
    </tr>
    <tr>
      <td>has_availability</td>
      <td>String</td>
      <td>Indicates whether the listing has any future availability.</td>
    </tr>
    <tr>
      <td>availability_30</td>
      <td>Int64</td>
      <td>Number of available nights in the next 30 days.</td>
    </tr>
    <tr>
      <td>availability_60</td>
      <td>Int64</td>
      <td>Number of available nights in the next 60 days.</td>
    </tr>
    <tr>
      <td>availability_90</td>
      <td>Int64</td>
      <td>Number of available nights in the next 90 days.</td>
    </tr>
    <tr>
      <td>availability_365</td>
      <td>Int64</td>
      <td>Number of available nights in the next 365 days.</td>
    </tr>
    <tr>
      <td>availability_eoy</td>
      <td>Int64</td>
      <td>Number of available nights from scrape date until the end of the calendar year.</td>
    </tr>
    <tr>
      <td>number_of_reviews_ly</td>
      <td>Int64</td>
      <td>Reviews received last year.</td>
    </tr>
    <tr>
      <td>estimated_occupancy_l365d</td>
      <td>Int64</td>
      <td>Estimated occupied nights in the last 365 days.</td>
    </tr>
    <tr>
      <td>estimated_revenue_l365d</td>
      <td>Float64</td>
      <td>Estimated occupied nights in the last 365 days.</td>
    </tr>
    <tr>
      <td>calendar_last_scraped</td>
      <td>String</td>
      <td>Date when the listing’s calendar was last scraped.</td>
    </tr>
    <tr>
      <td>number_of_reviews</td>
      <td>Int64</td>
      <td>Total number of reviews received by the listing.</td>
    </tr>
    <tr>
      <td>number_of_reviews_ltm</td>
      <td>Int64</td>
      <td>Number of reviews received in the last 12 months.</td>
    </tr>
    <tr>
      <td>number_of_reviews_l30d</td>
      <td>Int64</td>
      <td>Number of reviews received in the last 30 days.</td>
    </tr>
    <tr>
      <td>first_review</td>
      <td>String</td>
      <td>Date of the first review for the listing.</td>
    </tr>
    <tr>
      <td>last_review</td>
      <td>String</td>
      <td>Date of the most recent review for the listing.</td>
    </tr>
    <tr>
      <td>review_scores_rating</td>
      <td>Float64</td>
      <td>Overall guest rating of the listing on a 1–5 scale.</td>
    </tr>
    <tr>
      <td>review_scores_accuracy</td>
      <td>Float64</td>
      <td>Rating for accuracy of the listing description.</td>
    </tr>
    <tr>
      <td>review_scores_cleanliness</td>
      <td>Float64</td>
      <td>Rating for cleanliness of the listing.</td>
    </tr>
    <tr>
      <td>review_scores_checkin</td>
      <td>Float64</td>
      <td>Rating for the check-in experience.</td>
    </tr>
    <tr>
      <td>review_scores_communication</td>
      <td>Float64</td>
      <td>Rating for host communication quality.</td>
    </tr>
    <tr>
      <td>review_scores_location</td>
      <td>Float64</td>
      <td>Rating for location quality.</td>
    </tr>
    <tr>
      <td>review_scores_value</td>
      <td>Float64</td>
      <td>Rating for value for money.</td>
    </tr>
    <tr>
      <td>license</td>
      <td>String</td>
      <td>Listing license or registration number, where applicable.</td>
    </tr>
    <tr>
      <td>instant_bookable</td>
      <td>String</td>
      <td>Indicates whether the listing can be booked instantly without host approval.</td>
    </tr>
    <tr>
      <td>calculated_host_listings_count</td>
      <td>Int64</td>
      <td>Number of listings owned by the host in the current city or region.</td>
    </tr>
    <tr>
      <td>calculated_host_listings_count_entire_homes</td>
      <td>Int64</td>
      <td>Number of entire-home listings owned by the host in the current city or region.</td>
    </tr>
    <tr>
      <td>calculated_host_listings_count_private_rooms</td>
      <td>Int64</td>
      <td>Number of private-room listings owned by the host in the current city or region.</td>
    </tr>
    <tr>
      <td>calculated_host_listings_count_shared_rooms</td>
      <td>Int64</td>
      <td>Number of shared-room listings owned by the host in the current city or region.</td>
    </tr>
    <tr style="border-bottom: 1px solid #000000ff;">
      <td>reviews_per_month</td>
      <td>Float64</td>
      <td>Average number of reviews per month over the lifetime of the listing.</td>
    </tr>
  </tbody>
</table>




# 3. Tools and Technologies

Several tools and technologies were used inside the project for various purposes; including pipeline orchestration, data processing, data ingestion, version control. The listed tools and how they are integrated within a dataflow diagram can be found under [Appendix 3.1](appendix-3.1). 

In any projects, it is vital for code to be version-controlled while enabling cross collaboration. Hence, we decided to use a Docker environment alongside GitHub for team members to contribute their codes, and merging everyone's contributions after a thorough validation by other teammates. 

Docker provides an lightweight environment by setting configurations inside a docker-compose.yml file. By pulling the right Docker images from the vast repository of official//user-contributed images developed and saved within Docker Hub, users can create containers from the images, link the containers together using Docker networks and mounted volumes for shared data. Referring to the dataflow diagram, Docker is responsible for setting up many services, including Apache Airflow, Apache Spark (PySpark), HDFS, Hive, Trino, PostgreSQL, Clickhouse which are all linked to each other. 

Git and GitHub combo allows neat version control done via simple Git commands. Once users added abew feature, or fix some issues, they can contribute to the shared GitHub repository found under [Appendix 3.2](appendix-3.2) by submitting a new branch. Once other users validated the code for testing purposes and approved it, GitHub allows for merging branches via clicking a few buttons. This simple branch-like structure within Git allows all users to stay up-to-date with the latest codebase by running **git pull**, while contributing their own branches that would not affect the main codebase by running **git push**.

Next, we decided to webscrap the data within Inside Airbnb using Python's built-in requests alongside BeautifulSoup for HTML parsing to look for the correct CSV's files to download. To integrate within Airflow for pipeline orchestration, we decided to create a Docker image using Dockerfile by pulling a Python image and installing necessary packages (such as **pandas**, **BeautifulSoup**) using a lightweight package manager, **uv**. The webscrapper will look inside the Inside Airbnb website and look for files that contain the "listings.csv.gz" keyword under selected towns (London, Bristol, Edinburgh) as parameters. After downloading the CSV's files, the webscrapper will also standardize the inconsistent schemas such as STRING and DOUBLE for same columns in different files. Finally, the webscrapper converts the datasets into parquet format for lightweight storage and integration with HDFS. The parquet files are stored locally partitioned by the extraction date and city, and mounted inside the Docker environment as can be found under [Appendix 3.3](appendix-3.3).

Following the ingestion of raw data, the data will be uploaded inside HDFS via Apache Spark. This part is known as the bronze layer where raw data is ingested into our data architecture. The data is later cleaned inside the silver layer using Apache Spark for deduplication, column formatting//cleaning, and removing rows that do not contain price values. Finally, the data is processed according to a **Star Schema** where we created two (2) dimension tables, hosts and listings and one (1) fact table, listings; this step is also known as the gold layer. The processed data are finally stored inside Apache Clickhouse, an OLAP columnar database that stores the data of each column independetly. Due to the nature of OLAP database, Clickhouse enables more efficient aggregation queries, and faster filtering due to Clickhouse's built-in MergeTree engine.  

In the meantime, the raw data and staging data inside Bronze and Silver layers respectively can be explored via familiar SQL queries. We decided to integrate Hive to create external tables reading the parquet files inside HDFS and storing the metadata within a PostgreSQL database. Users can explore and troubleshoot the data, should there be issues found within the downstream data using Trino, which is connected to Hive but offers faster, and interactive analytics by bypassing MapReduce for lower-latency queries. Both Clickhouse and Trino SQL queries can be executed within the terminal by using Docker to connect to the individual containers; but we decided to expose both Clickhouse's and Trino's ports to local PC, and using a popular database management tool that serves a SQL client and IDE to manage queries, that offers a simplistic UI for data browsing, SQL editing, known as dbeaver that is installed from the native Microsoft Store (for Windows user). 

The processed data is visualized using Microsoft's Power BI (similarly installed from Microsoft Store), Power BI can be integrated with multiple data storages, including but not limited to Clickhouse, Trino, MySQL, S3 Object Storage by installing the necessary drivers. Furthermore, Power BI offers a drag-and-drop user-friendly UI that can be used to create interactive, cross-filtering dashboards. In this project, Power BI is used to connect to the processed data inside Clickhouse and visualizes key metrics such as **average review ratings**, **number of verified hosts**, **number of listings from London, Edinburgh, Bristol**. The snapshot of the Power BI dashboard can be found under [Appendix 3.4](appendix-3.4).

Last but not least, the ELT pipeline can be orchestrated and ran with a single button-click thanks to Apache Airflow. A DAG, or Directed Acyclic Graph is set-up within Airflow to represent the tasks from raw data ingestion via webscrapping to uploading the data within HDFS to processing and finally loading the data into Clickhouse. Airflow also enables scheduling, such as rerunning the entire pipeline every fixed hours, or days, vital for automation of data pipeline in the real world. 

# 5. Conclusion

This concludes the Airbnb ELT project from raw data ingestion to data visualization and analysis. 

For future work, many tools can be further integrated within the pipeline to enable a smoother, more efficient ELT projects. For example, as data size grows, storing the data locally is not a feasible option, and hence should be stored inside a **Cloud Object Storage**, such as S3 offered by AWS, and Google Cloud Storage (GCS) offered by Google Cloud Platform (GCP) whereas Spark will just directly read from the Cloud.

Furthermore, referring to the **Variety** of 7V's of Big Data, Airbnb data contains multiple types of unstructured data, such as user reviews and listing photos. Hence, the project can be further upgraded to support unstructured data using tools such as a NoSQL database, object storage for a data lake or lakehouse approach using Apache Iceberg. As the volume of data inevitably increase, Cloud options should be comprehensively explored for a more resource optimized and cost savings approach, such as using services offered by AWS (Glue, S3, Lambda) for a more robust pipeline that offers high fault tolerance and availability via distribution of computing resources across multiple regions on the planet.


# Appendix

## 3. Tools and Technologies


### Appendix-3.1

![appendix-3-1](readme_images/data_architecture.png)