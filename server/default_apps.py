from models import Application
import json
from setup_app_database import get_all_applications




def skill_set():
    """
    Set of all relevant skills that a person could have in their resume.
    """
    skill_set = {".NET", ".Net", "AD", "ADAS", "ADC", "AI", "AI/ML", "AJAX", "API", "APIs", "ASP.NET", "AST", "AWS", "Access", "Accessibility", "Accountability", "Accounting", "Accuracy", "Action-oriented", "Adapt", "Adaptability", "Adaptable", "Adobe", "Agile", "Agility", "Algorithms", "Altium", "Analytical", "Android", "Angular", "AngularJS", "Animation", "Ansible", "Antennas", "Appium", "Arduino", "Attendance", "Attitude", "Authentication", "AutoCAD", "AutoCad", "Automation", "Autonomy", "Azure", "BaBel", "Babylon.js", "Backend", "Bash", "Bash/Shell", "Bidding", "Bioinformatics", "Bitbucket", "Boost", "Bugzilla", "C", "C#", "C#/.NET", "C+", "C++", "C++/C#", "C/C++", "C/c++", "CI/CD", "CICD", "CIGI", "CMake", "CPT", "CSS", "CSS3", "CUDA", "Cadence", "Calculus", "Canva", "CarMaker", "CarSim", "Charismatic", "Chromium", "Clang", "Closures", "Coaching", "Coding", "Collaboration", "Collaborative", "Collaborator", "Commitment", "Committed", "Communication", "Communicator", "Competitions", "Compiler", "Compilers", "Confidentiality", "Confluence", "Consulting", "Containerization", "Containers", "Contentful", "Creativity", "Cross-Compilation", "Curiosity", "Curious", "Cybersecurity", "DB2", "DHCP", "DNS", "DSP", "Dagger", "Dash", "Dashboarding", "Dashboards", "Data-driven", "Database", "Databases", "Datasheets", "Debuggers", "Debugging", "Decisiveness", "Dedication", "DeltaLake", "Dependability", "Dependable", "Deployment", "Detail-oriented", "Determination", "DevOps", "DevSecOps", "Direct3D", "Discipline", "Django", "Django/Flask", "Docker", "Documentation", "Drive", "Driven", "DynamoDB", "EJB", "ES5/6", "ESRI", "Eagerness", "Eclipse", "Economics", "Efficient", "ElasticSearch", "Elasticsearch", "Electromagnetics", "Electron", "Electronic", "Electronics", "Elixir", "Embedded", "Empathetic", "Emulators", "Engagement", "Enthusiastic", "Entrepreneurial", "Etcd", "Ethernet", "Excel", "Excellence", "Exchange", "Excited", "ExoPlayer", "Express", "FFmpeg", "FPGA", "Figma", "FinTech", "Finance", "Flask", "Flexibility", "Flexible", "Flink", "Flutter", "Focus", "Follow-up", "Fortran", "Frontend", "Fullstack", "Fun", "GDAL", "GED", "GIS", "GIT", "GPIO", "GSEC", "GStreamer", "GenAI", "Genomics", "Git", "GitHub", "GitLab", "Github", "Gitlab", "Go", "GoLang", "Goal-oriented", "Golang", "GoogleTest", "GraphQL", "Greater", "Greenhills", "Grit", "Groovy", "Gulp", "HBase", "HTML", "HTML-5", "HTML/CSS", "HTML/CSS/JS", "HTML5", "HTTP", "HYDE", "Hadoop", "Hard-working", "Hibernate", "Higher", "Hive", "Honest", "Hootsuite", "Houdini", "Hudi", "Humble", "HydroCad", "Hypervisor", "I2C", "IIS", "IOS", "IP", "IT/Networking", "IText", "Iceberg", "Inclusivity", "Independence", "Influencing", "Informatica", "Initiative", "Innovate", "Innovation", "Innovative", "Inquisitive", "Integration", "Integrity", "Interested", "Internships", "Interpersonal", "Investment", "JEE", "JIRA", "JQuery", "JSON", "JSP", "JUnit", "Java", "JavaScript", "Javascript", "Jenkins", "Jira", "Kafka", "Kanban", "Kokkos", "Kotlin", "Kubernetes", "Kudu", "LLMs/RAG", "LLVM", "LabVIEW", "Laravel", "Layouts", "Leadership", "Leaflet", "Libraries", "Linux", "Linux/UNIX", "Linux/Unix", "Linux/Windows", "Lit", "Logstash", "Lync", "MATLAB", "MIL/SIL", "MIS", "MLE", "MLIR", "MPI", "MQ", "MQTT", "MSSQL", "MVC", "MVVM", "MacOS", "MapBox", "MariaDB", "MathCad", "Mathematics", "Matlab", "Maya", "Mentoring", "Microcontrollers", "Microservices", "Microsoft.net", "Mil-Std-1553", "Model-View-Controller", "Modeling", "Modems", "MongoDB", "Motivated", "Motivation", "Multi-Threading", "Multi-tasking", "Multitasking", "Multithreading", "MxNET", "MySQL", "NSQ", "NUnit", "Networks", "Next.js", "NiFi", "NoSQL", "Node.js", "NodeJS", "Numpy", "Nutanix", "OOA/OOD", "OOP", "OPT", "ORC", "OSGi", "Object-Oriented", "Objective-C", "Objective-c", "Objectivity", "Ooad", "Open-Minded", "OpenCL", "OpenGL", "OpenLayers", "OpenMP", "Operations", "Oracle", "OracleDB", "Orchestration", "Orekit", "Organization", "Organizational", "Organized", "Oscilloscopes", "Ownership", "PADS", "PAN-OS", "PCIe", "PHP", "PHP/MySQL", "PWM", "Pandas", "Parquet", "Passion", "Passionate", "Patience", "Paxos", "Perforce", "Perl", "Perseverance", "Persistence", "Photoshop", "Physics", "Playback", "Portable", "PostGIS", "PostgreSQL", "Postgres", "PowerApps", "PowerBI", "PowerPoint", "Presentation", "Prioritize", "Proactive", "Proactivity", "Probability", "Problem-Solving", "Problem-solving", "Production", "Professionalism", "Programming", "Protocols", "Prototyping", "Punctual", "Punctuality", "Puppet", "PyTorch", "Python", "Qnx", "Qt", "Quant", "Queuing", "R", "RAG", "RDBMS", "REST", "RF", "ROS", "RS-232", "RS-422", "RTOS", "RabbitMQ", "Raft", "Rails", "Rancher", "Ranking", "React", "React.js", "ReactJS", "ReactNative", "Redis", "Redux", "Relationship-building", "Reliability", "Research", "Resourceful", "Responsibility", "Responsible", "Results-oriented", "Reusable", "Rhapsody", "Rigour", "Robotics", "Rollup", "Router", "Ruby", "Rust", "SAP", "SCCM", "SDLC", "SIMD", "SOA", "SPI", "SQL", "SQS", "SSCP", "SSRS", "STEM", "SVN", "SYCL", "Scala", "Scalability", "Schematics", "Scripting", "Scrum", "ScyllaDB", "Security", "Security+ce", "Selenium", "Self-Awareness", "Self-Confidence", "Self-Directed", "Self-Driven", "Self-Learning", "Self-Motivated", "Self-Motivation", "Self-Starter", "Self-discipline", "Self-driven", "Self-motivated", "Self-motivation", "Self-starter", "Servlets", "SharePoint", "Shoelace", "Simulation", "Simulations", "Simulators", "Simulink", "Smart", "SolidWorks", "Spark", "Specificity", "Spinnaker", "Spring", "Springboot", "Stateflow", "Statistics", "Storage", "Subversion", "Supercomputing", "Swift", "SwiftUI", "Switch", "Sybase", "Symfony", "Synthesis", "T-SQL", "TCL", "TCP", "TCP/IP", "TDD", "TVM", "Tableau", "Team-Oriented", "Team-oriented", "TeamCity", "Teamwork", "TensorFlow", "Tensorflow", "Terraform", "TestRail", "Testing", "Thoroughness", "Threads", "Threats", "Three.js", "Thrive", "Timeliness", "Torch", "Trading", "Transcoding", "Troubleshooting", "TurboCAD", "Tutoring", "TypeScript", "Typescript", "Typing", "UDP", "UML", "USB", "Unity", "Unix", "Unix/Linux", "Unix/linux", "Unreal", "Usability", "V8", "VLC", "VMWare", "VSphere", "Virtualization", "Visio", "Visualization", "Vue", "Vue.js", "Vulkan", "VxWorks", "WPF", "WaterCad", "Webpack", "Windows", "Wireless", "Wix", "Word", "WordPress", "Wordpress", "Workflows", "XLA", "XML", "XML/XSLT", "XrmToolBox", "Zero-MQ", "ZooKeeper", "a* search", "accountability", "actionscript", "active listening", "adaptability", "advertisement marketing", "agile", "agility", "ai", "ai ethics", "ai model training", "ai-enhanced experiences", "airflow", "airflow for ml", "airtable", "algorithms", "alibaba cloud", "amazon rds", "android", "android jetpack", "angular", "ansible", "ant colony optimization", "apache", "api development", "api testing", "app engine", "application security", "applitools", "approximation algorithms", "ar/vr", "argo cd", "argocd", "arrays", "asana", "asp.net", "assembly", "assertiveness", "attention span", "attention to detail", "aurora", "automation scripting", "autonomy", "avl tree", "aws", "aws api gateway", "aws lambda", "azure", "azure devops", "azure functions", "azure logic apps", "azure ml", "backblaze", "backbone.js", "backend as a service", "backtracking", "bamboo", "basecamp", "bash", "bash scripting", "bdd", "bellman-ford", "bfs", "big data", "big-o notation", "bigquery", "binary indexed tree", "binary search tree", "bind", "binomial heap", "bipartite graph", "bit manipulation", "bitbucket", "blazemeter", "blazor", "blockchain basics", "bootstrap", "boyer-moore", "branch and bound", "browserstack", "bugzilla", "bulma", "burp suite", "business acumen", "c#", "c++", "camera x", "career development", "carina", "cartesian tree", "cassandra", "catboost", "ceh", "ceph", "chai", "chatbots", "chatgpt", "checkmarx", "chef", "ci/cd", "circleci", "cissp", "clickhouse", "clickup", "clojure", "cloud computing", "cloud firestore", "cloud foundry", "cloud functions", "cloud run", "cloud security", "cloud-init", "cloudflare", "coaching", "cobol", "code review", "coffeescript", "colab", "collaboration", "collaborative problem solving", "commitment", "communication", "compliance", "computer vision", "concentration", "confidentiality", "conflict resolution", "confluence", "consul", "contentful", "continuous deployment", "continuous integration", "continuous learning", "conversational ai", "cordova", "core data", "cortex xdr", "couchbase", "couchdb", "creativity", "critical thinking", "cron", "cross-browser compatibility", "cross-functional collaboration", "crowdstrike", "css", "cucumber", "cultural awareness", "customer focus", "cybersecurity", "cypress", "dagger", "daisyui", "dancing links", "darktrace", "dart", "dask", "dast", "data analysis", "data mining", "data privacy", "data science notebooks", "data structures", "data visualization", "databricks", "databricks notebooks", "datadog", "dataiku", "db2", "decision making", "dedication", "deep learning", "deepfake detection", "delegation", "dependability", "design thinking", "detail-oriented", "determination", "dfs", "dhcp", "digital literacy", "digitalocean", "dijkstra's algorithm", "disjoint set", "divide and conquer", "django", "dns", "docker", "docker swarm", "documentation", "drone", "drupal api", "dvc", "dynamic connectivity", "dynamic programming", "dynamodb", "edge ai", "edge computing", "edit distance", "edmonds-karp", "elasticsearch", "elixir", "ember.js", "emotional intelligence", "emotional regulation", "empathy", "encryption", "end-to-end testing", "energy", "ensemble learning", "enthusiasm", "entrepreneurial mindset", "entrepreneurship", "enzyme", "erlang", "etcd", "ethical hacking", "ethics", "eventbridge", "excel", "explainable ai", "express", "fairness in ai", "fargate", "feature engineering", "feedback", "fenwick tree", "fetch.ai", "fibonacci heap", "fibonacci sequence", "figma", "firebase", "firewall management", "firewalld", "firewalls", "flask", "flexibility", "flink", "floyd-warshall", "flutter", "focus", "ford-fulkerson", "forensics", "fortinet", "fortran", "foundation", "function as a service", "functional data structures", "functional testing", "gale-shapley", "gatling", "gcp", "gdpr", "genetic algorithms", "git", "gitflow", "github", "github actions", "gitlab", "gitlab ci", "glusterfs", "go", "goal setting", "google cloud", "google cloud functions", "google gemini", "google maps api", "grafana", "graph coloring", "graph neural networks", "graph theory", "graph traversal", "graphql", "greedy algorithms", "greenplum", "grit", "groovy", "growth mindset", "grpc", "h2o.ai", "hadoop", "haproxy", "hash tables", "haskell", "hbase", "headless cms", "heap", "helm", "heroku", "hilt", "hipaa", "hive", "honesty", "html", "humility", "hyper-v", "hyperparameter tuning", "ibm cloud", "ids/ips", "image recognition", "incident response", "inclusivity", "independence", "influxdb", "initiative", "innovation", "integer programming", "integration testing", "integrity", "interpersonal skills", "interval tree", "ionic", "ios", "iot", "iptables", "isc dhcp", "iscsi", "iso 27001", "iso 27017", "java", "java (android)", "javascript", "jenkins", "jenkins x", "jest", "jetpack compose", "jira", "jmeter", "json", "json api", "json-rpc", "junit", "jupyter notebooks", "jwt", "k6", "kafka", "kaggle", "kali linux", "kanban", "keepalived", "keras", "key management", "kindness", "kmp algorithm", "knapsack problem", "knime", "knockout.js", "koin", "kotlin", "kruskal's algorithm", "kubeflow", "kubernetes", "kubernetes for ml", "kvm", "lambda edge", "lambda@edge", "laravel", "lazy propagation", "leadership", "learning agility", "leftist heap", "lifelong learning", "lightgbm", "linear programming", "linked lists", "linode", "linux", "load balancing", "load testing", "loadrunner", "locust", "logrotate", "longest common subsequence", "lottie", "lua", "luigi", "lxc/lxd", "machine learning", "mahout", "manacher's algorithm", "marionette.js", "matching algorithms", "material-ui", "matlab", "matplotlib", "maximum flow", "mentorship", "mercurial", "metasploit", "microsoft azure", "microsoft office", "microsoft sql server", "microsoft teams", "min-cost max-flow", "mindfulness", "minimum cut", "minimum spanning tree", "mithril.js", "ml kit", "ml pipelines", "mlflow", "mllib", "mlops", "mocha", "model deployment", "monday.com", "mongodb", "monotonic stack", "monte carlo method", "multitasking", "multithreading", "mysql", "nagios", "native script", "natural language processing", "negotiation", "neo4j", "nessus", "netcat", "netlify", "network flow", "network security", "networking", "neural networks", "new relic", "next.js", "nfs", "nginx", "nist", "nlp", "nltk", "nmap", "nomad", "notion", "numpy", "nuxt.js", "oath", "oauth", "oauth2", "objective-c", "octopus deploy", "okhttp", "online algorithms", "openapi", "opencv", "openid connect", "openshift", "openstack", "openvas", "openvpn", "oracle", "oracle cloud", "organization", "oscp", "ovh", "ovh cloud", "owasp", "ownership", "packer", "pact", "pair programming", "pairing heap", "pandas", "passion", "patience", "paypal api", "pci dss", "penetration testing", "performance testing", "perl", "perseverance", "persistence", "persistent data structures", "personal branding", "personal development", "personalized experiences", "phabricator", "php", "pig", "pivotal tracker", "positivity", "postgresql", "postman", "powerpoint", "powershell", "presentation skills", "prioritization", "priority queue", "proactivity", "problem solving", "problem-solving", "product management", "professionalism", "project management", "project planning", "prometheus", "proxy servers", "public speaking", "puppet", "puppet enterprise", "push-relabel", "pyspark", "pytest", "python", "pytorch", "qtest", "quantum computing basics", "queues", "r", "rabin-karp", "rackspace", "rails", "rancher", "randomized algorithms", "range queries", "rapidminer", "rational functional tester", "react", "react native", "realm", "realm database", "recommender systems", "recursion", "red-black tree", "redis", "redmine", "redshift", "reflection", "reinforcement learning", "reliability", "remote collaboration", "resilience", "resource management", "respect", "responsibility", "responsive design", "rest", "restful api", "retrofit", "revenue generation", "risk management", "robot framework", "robotics", "room", "rpc", "rsync", "ruby", "rust", "rxjava", "rxkotlin", "rxswift", "sagemaker", "salesforce", "salesforce api", "saltstack", "samba", "saml", "sap cloud", "sast", "saucelabs", "scala", "scheme", "scikit-learn", "scrum", "seaborn", "search algorithms", "secure coding", "security auditing", "security testing", "segment tree", "selenium", "self-adjusting data structures", "self-awareness", "self-discipline", "self-motivation", "self-reliance", "self-starter", "semantic-ui", "serverless architecture", "service bus", "shell", "shopify api", "siem", "simplex algorithm", "simplify", "simulated annealing", "skip list", "slack", "smart cities", "smart home", "snowflake", "sns", "snyk", "soap", "soapui", "soc2", "social media", "solr", "sorting algorithms", "space complexity", "spark", "speech recognition", "speech-to-text", "spinnaker", "splunk", "splunk phantom", "spring", "sql", "sqlite", "sqs", "ssl/tls", "sso", "stable matching", "stacks", "step functions", "strapi", "strategic thinking", "stress management", "stress testing", "stripe api", "suffix tree", "svelte", "svn", "swagger", "swift", "swiftui", "sybase", "symfony", "synthetic data", "system monitoring", "systemd", "taiga", "tailwind", "tailwind css", "tailwindcss", "taskwarrior", "tau", "tcp/ip", "tcpdump", "tdd", "team building", "team spirit", "teamcity", "teamwork", "tech savviness", "technical writing", "tekton", "tenable.io", "tenacity", "tencent cloud", "tensorflow", "teradata", "terraform", "test automation", "testcomplete", "testng", "text-to-speech", "threat modeling", "thrift", "tiktok ad campaigns", "time complexity", "time management", "timeboxing", "timescale db", "todoist", "tolerance", "topological sorting", "trac", "travis ci", "treap", "trees", "trello", "trie", "trustworthiness", "typescript", "uddi", "union-find", "unit testing", "unix", "user empathy", "user experience enhancement", "ux/ui design", "vagrant", "vault", "veracode", "vercel", "vertex ai", "vertica", "vertical search model", "video processing", "virtual teams", "virtualbox", "visual basic", "vmware", "voice assistants", "volley", "vpn", "vue.js", "vulnerability assessment", "vultr", "wasabi", "web accessibility", "web design", "web scraping", "webhooks", "windows server", "wireguard", "wireshark", "wordpress api", "work ethic", "work-life balance", "workmanager", "wsdl", "xamarin", "xen", "xgboost", "xml", "xray", "yolov5", "youtrack", "z algorithm", "zabbix", "zephyr", "zero trust"}

    return skill_set


"""
## Code to extract all new skills from applications data
with open('server/application_data/extracted_swe_jobs.json', 'r') as file:
    job_data = json.load(file)
    new_skill_set = skill_set()
    for job in job_data:
        for skill in job['skills']:
            if ' ' not in skill:
                if skill not in skill_set():
                    new_skill_set.add(skill)
    sorted_skill_list = sorted(list(new_skill_set))
    with open('skill_set.json', 'w') as file:
        json.dump(sorted_skill_list, file)
"""
                

def default_apps(google_id):
    """
    Returns default applications that a user will have in their table once registering an account. 
    """
    get_all_applications()
    default_apps = get_all_applications()


    return (
        
        
        [
    Application(status="Not Applied", name="Akuna Capital", open="Software Engineer Intern - Python", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Jane Street", open="Software Engineer Internship", close="New York, NY", link="", google_id=google_id),
    Application(status="Not Applied", name="Wells Fargo", open="Software Engineering Intern", close="Multiple locations", link="", google_id=google_id),
    Application(status="Not Applied", name="TikTok", open="Mobile Software Engineer Intern - User Relation", close="Los Angeles, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="IXL Learning", open="Software Engineer, Intern", close="San Mateo, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="ATPCO", open="Systems Engineer Intern", close="Remote in USA", link="", google_id=google_id),
    Application(status="Not Applied", name="ATPCO", open="Systems Engineer Intern", close="Dulles, VA", link="", google_id=google_id),
    Application(status="Not Applied", name="Sensata", open="Software Engineer Intern - Summer 2025", close="Attleboro, MA", link="", google_id=google_id),
    Application(status="Not Applied", name="Akuna Capital", open="Quantitative Research Intern - Summer 2025", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Amazon", open="Program Manager Intern", close="Seattle, WA", link="", google_id=google_id),
    Application(status="Not Applied", name="Virtu Financial", open="Internship - Developer", close="NYC", link="", google_id=google_id),
    Application(status="Not Applied", name="ByteDance", open="Software Engineer Intern (AI Platform)", close="San Jose, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="Notion", open="Software Engineer Intern, Mobile (Summer 2025)", close="New York, NY", link="", google_id=google_id),
    Application(status="Not Applied", name="Notion", open="Software Engineering Intern (Summer 2025)", close="San Francisco, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="Motorola", open="Android Platform Software Engineering Intern - Summer 2025", close="Plantation, FL", link="", google_id=google_id),
    Application(status="Not Applied", name="Motorola", open="Android Platform Software Engineering Intern - Summer 2025", close="Hoffman Estates, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Codeium", open="Software Engineering Intern - Summer 2025", close="Mountain View, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="HPR (Hyannis Port Research)", open="Software Engineering Intern - Summer 2025", close="Needham, MA", link="", google_id=google_id),
    Application(status="Not Applied", name="Sentry", open="Software Engineer Intern - Summer 2025", close="Toronto, ON, Canada", link="", google_id=google_id),
    Application(status="Not Applied", name="Ventas", open="Intern, Software Engineering (Summer 2025)", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Five Rings", open="Software Developer Intern", close="New York", link="", google_id=google_id),
    Application(status="Not Applied", name="Confluent", open="Software Engineering Intern", close="Remote", link="", google_id=google_id),
    Application(status="Not Applied", name="Confluent", open="Software Engineering Intern", close="Austin, TX", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern - 2025", close="Bellevue, WA", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern - 2025", close="Mountain View, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern - 2025", close="SF", link="", google_id=google_id),
    Application(status="Not Applied", name="Deloitte", open="Software Engineering Summer Scholar", close="New York, NY", link="", google_id=google_id),
    Application(status="Not Applied", name="Deloitte", open="Software Engineering Summer Scholar", close="Austin, TX", link="", google_id=google_id),
    Application(status="Not Applied", name="Deloitte", open="Software Engineering Summer Scholar", close="San Francisco, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="TikTok", open="Software Engineer Intern (Data-TnS-Eng-Biz Arch)", close="Vancouver, Canada", link="", google_id=google_id),
    Application(status="Not Applied", name="Airwallex", open="Software Engineer Intern Program", close="SF", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern", close="Bellevue, WA", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern", close="Mountain View, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="Databricks", open="Software Engineering Intern", close="San Francisco, CA", link="", google_id=google_id),
    Application(status="Not Applied", name="Strider Technologies", open="Intelligence Specialist Internship - China Focus", close="Vienna, VA", link="", google_id=google_id),
    Application(status="Not Applied", name="Strider Technologies", open="Intelligence Specialist Internship - China Focus", close="South Jordan, UT", link="", google_id=google_id),
    Application(status="Not Applied", name="Oshkosh", open="Data Engineer Intern - Advanced Analytics", close="Oshkosh, WI", link="", google_id=google_id),
    Application(status="Not Applied", name="Quantiq Partners", open="Software Developer Intern", close="Austin, TX", link="", google_id=google_id),
    Application(status="Not Applied", name="Belvedere Trading", open="Software Engineer Intern - Summer 2025", close="Boulder, CO", link="", google_id=google_id),
    Application(status="Not Applied", name="Belvedere Trading", open="Software Engineer Intern - Summer 2025", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Jump Trading", open="Campus Web Dev / UI Software Engineer – Intern", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Neuralink", open="Software Engineer Intern", close="Austin, TX", link="", google_id=google_id),
    Application(status="Not Applied", name="DV Trading", open="2025 Summer Internship - Algo Trader", close="Chicago, IL", link="", google_id=google_id),
    Application(status="Not Applied", name="Qualcomm", open="Software Engineering Intern", close="San Diego, California", link="", google_id=google_id),
    Application(status="Not Applied", name="Vestmark", open="Software Engineer Intern", close="Wakefield, MA", link="", google_id=google_id),
    Application(status="Not Applied", name="Epic", open="Software Developer Intern", close="Madison, WI", link="", google_id=google_id),
    Application(status="Not Applied", name="Apple", open="Machine Learning Intern", close="United States", link="", google_id=google_id)
])

print(get_all_applications())