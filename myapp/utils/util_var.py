phase_questions = [
    # generic questions
    "Is the application you're planning to build a web application, a mobile application, or a desktop application?",
    "Will this application be cross-platform, or are you targeting a specific operating system or device?",
    "Will your application require a database to store and manage data?",
    "If so, do you have any preferences for the type of database (e.g., SQL, NoSQL)?",
    "Are there specific APIs or external services you plan to use?",
    "What level of security measures do you need to implement (e.g., data encryption, secure user authentication)?",
    "Does your application need to support real-time features (e.g., live updates, real-time collaboration)?",
    "Do you need to include data analytics or reporting features in your application?",
    "Will users be able to generate reports or visualize data within the application?",
    "Do you have specific requirements or preferences for the user interface and design of the application?",
    "Are there any existing design guidelines or brand standards you need to follow?"
    # Project Setup
    "What are the main objectives and goals of the project?",
    "what kind of technologies will be used to complete this project?",
    "Who are the key stakeholders and what are their roles?",
    "What is the initial project scope and deliverables?",
    "What resources are available for the project (team, tools, budget)?",
    "What are the initial risks identified and how will they be managed?",
    "What are the success criteria for this project?",
    # Discovery Phase
    "What are the primary problems or needs that the project aims to address?",
    "Who are the end-users and what are their specific needs?",
    "What is the competitive landscape and market trends relevant to the project?",
    "What are the existing systems or solutions that the project will interact with?",
    "What are the key constraints or limitations affecting the project?",
    # Develpoment Phase
    "What are the steps for deploying the software to the production environment?",
    "How will data migration be handled, if applicable?",
    "What are the configuration management and environment setup requirements?",
    "How will the deployment be validated and verified?",
    # Integration Phase
    "How will different system components and services be integrated?",
    "What are the key integration points and dependencies?",
    "How will integration testing be performed and validated?",
    # Deployment Phase
    "What is the release plan and schedule for the software?",
    "How will the deployment process be managed and monitored?",
    "What are the post-deployment support and maintenance procedures?",
    "Do you have any preferences for how and where the application will be deployed and hosted?",
    "Are you considering cloud services for hosting and scaling the application?",
    # Access Control
    "What authentication and authorization mechanisms will be used?",
    "How will user roles and permissions be defined and managed?",
    "What are the security policies and procedures for access control?",
    "How will compliance with regulations and standards be ensured?",
    # Maintenance Phase
    "What is the plan for monitoring and maintaining the software?",
]
project_phases = """
1. Project Setup:
   Description: ```here you need to describe simple tools and technologies setup you required for implemenating the application. Try to go in detail when setting up enviroment and configration based on stack described by user.```

3. Discovery Phase:
   Description: ```Based on the given context Gather  information regarding specific use cases and cater client needs and making SRS docmunetation making Low level architecture daigram, class daigram, use case daigram based on the client requirmenets```

5. Development Phase:
   Description: ```here just give client an idea how development will take place don't go into too much detail here . if possible just add name of phase and skip other parts ```

6. Integration Phase:
   Description: ```here you need to go into much detail about different integration of different modules feel free to go into as much detail as possible from technical point of view . Ensure that all components and module of app like front-end and backend are integrated smoothlhy, integration might also include any third party integration from inference calls, cloud api, connecting with databases etc```

8. Deployment Phase:
   Description: ```here you need to give a complete idea based on application stack how deployement will take place.Based on the given context how the app is supposed to deploy based on the given context what are options provided by user and what are some you can assume user will app will need in this particular case```

9. Access Control:
   Description:Based on the context Manage and secure user access to the system. Define user roles and permissions based on job functions and security requirements. Implement authentication and authorization mechanisms to control access. Regularly review and update access controls to reflect changes in user roles or organizational policies. Ensure compliance with security standards and best practices.

10. Maintenance Phase:
    Description: BAsed on the conetxt what modules will require maintaince and what kind of maitainance they will require try to add as many  assumptions you think it will need and also see user needs for this as well and provided suggestion in context

"""

questions = [
    "will this application require authentication module like login,signup and recovery password for every user?",
    "Is the application you're planning to build a web application, a mobile application, or a desktop application?",
    "Will this application be cross-platform, or are you targeting a specific operating system or device?",
    "Will your application require a database to store and manage data?",
    "What are the main modules or components of the application? List all.",
    "Can you provide a detailed description of each main module or component of the application?",
    "What is the primary function and goal of each module? List all.",
    "What are the specific features and functionalities that each module will provide. Start from from high level features to low level features try to go into as small implemenatation details as possible?List all.",
    " Who are the intended users of each module, and what permissions or roles will they have? List all.",
    "What data will each module receive as input, and what will it produce as output? List all.",
    "How does each module interact with other modules or external systems? Are there any dependencies that need to be considered? List all.",
    "What are the key UI elements and design considerations for each module? List all.",
    "Are there any specific technical requirements or constraints for each module, such as performance, security, or compliance standards? List all.",
    "What APIs or integration points will be necessary for each module to function correctly? List all.",
    "What considerations should be made for scaling each module, and are there any planned future enhancements? List all.",
    "What are the expected performance metrics for each module, such as response time, throughput, and latency? List all.",
    "What security measures need to be in place for each module, such as encryption, authentication, and authorization? List all.",
    "If so, do you have any preferences for the type of database (e.g., SQL, NoSQL)?",
    "Are there specific APIs or external services you plan to use?",
]
feature_template = """
Software Feature Breakdown Guide

You are a Senior Software Engineer tasked with extracting and refining features from a sample estimation sheet for a software project. Additionally, you have access to user-provided questions and answers regarding the estimation sheet to aid in accuracy. Your goal is to:

1. Identify and Extract All Possible Features:
    - Review the estimation sheet thoroughly.
    - Identify distinct features or modules mentioned.
    - Extract these features for further analysis.

2. Ensure Technical Detail and Viability:
    - For each feature, break it down into the smallest possible sub-functionalities.
    - Verify that each sub-functionality is technically detailed and viable for implementation.
    - Ensure each sub-functionality has clear requirements and can be developed independently.

3. Rename Features for Compatibility:
    - Ensure that feature names are clear, concise, and align with standard application development practices.
    - Rename features if necessary to improve clarity and compatibility with development processes.

4. Address Additional Aspects:
    - Consider deployment strategies for the project.
    - Identify any data migration requirements.
    - Plan for integration with existing systems if applicable.

Steps to Break Down Each Module into Sub-Functionalities

1. Identify the Core Purpose:
    - Understand the main objective of the module.
    - Define the primary functionality it needs to achieve.

2. List High-Level Features:
    - Break down the core purpose into high-level features.
    - Each high-level feature should represent a significant part of the module's functionality.

3. Decompose High-Level Features:
    - For each high-level feature, identify smaller sub-features or components.
    - Ensure these sub-features are as granular as possible.

4. Define Sub-Functionalities:
    - For each sub-feature, define the specific actions, processes, or tasks it will perform.
    - Ensure each sub-functionality is a single, discrete task.

5. Detail Technical Requirements:
    - Specify the technical requirements for each sub-functionality.
    - Include details such as input/output, processing logic, data handling, and any dependencies.

6. Validate Viability:
    - Verify that each sub-functionality is feasible within the project scope.
    - Check for any technical constraints or limitations.

7. Rename for Clarity:
    - Ensure that the names of sub-functionalities are clear and descriptive.
    - Rename as necessary for better clarity and understanding.

Example Breakdown

Module: User Management

1. Core Purpose:
    - Manage user accounts and access levels.

2. High-Level Features:
    - User Registration
    - User Authentication
    - User Profile Management
    - Access Control

3. Decomposing High-Level Features:

    - User Registration:
        - Input validation
        - Duplicate account check
        - Email verification
        - Store user data in database

    - User Authentication:
        - Login form
        - Password encryption
        - Session management
        - Multi-factor authentication

    - User Profile Management:
        - View profile
        - Edit profile details
        - Change password
        - Upload profile picture

    - Access Control:
        - Define roles and permissions
        - Assign roles to users
        - Permission validation for actions
        - Role-based access control

4. Defining Sub-Functionalities:

    - Input Validation:
        - Check required fields
        - Validate email format
        - Ensure strong password

    - Duplicate Account Check:
        - Search existing users by email
        - Return error if duplicate found

    - Email Verification:
        - Generate verification token
        - Send verification email
        - Verify token on user click

    - Store User Data:
        - Save user details to database
        - Encrypt sensitive data

    - Login Form:
        - Create login form UI
        - Validate user input
        - Submit login request

    - Password Encryption:
        - Hash passwords
        - Store hashed passwords securely

    - Session Management:
        - Create user session on login
        - Store session token
        - Validate session on each request

    - Multi-Factor Authentication:
        - Send OTP via email/SMS
        - Verify OTP on user input

    - View Profile:
        - Fetch user data from database
        - Display user data on profile page

    - Edit Profile Details:
        - Form to edit profile details
        - Validate updated details
        - Save changes to database

    - Change Password:
        - Form to change password
        - Validate current and new passwords
        - Update password in database

    - Upload Profile Picture:
        - Form to upload picture
        - Validate image format/size
        - Save image to server

    - Define Roles and Permissions:
        - Create roles (admin, user, etc.)
        - Define permissions for each role

    - Assign Roles to Users:
        - Interface to assign roles
        - Save role assignments in database

    - Permission Validation:
        - Check user permissions on actions
        - Restrict actions based on permissions

    - Role-Based Access Control:
        - Implement role-based access checks
        - Ensure secure access control

5. Detail Technical Requirements:
    - For each sub-functionality, specify the inputs, outputs, processing logic, and dependencies.

6. Validate Viability:
    - Ensure each sub-functionality is technically feasible and aligns with project scope.

7. Rename for Clarity:
    - Ensure all names are clear and understandable.

Using Queries and Answers

Example User Queries and Answers:

{user_queries}

Output Format:

{format_instructions}
"""


fix_array_template = """
I am providing you with a string that contain answers with their numbers i want you to convert it into sepcific format provided to you:

Answers in string:
```{answers}```

Format to be converted to:
{format_instructions}
"""

qa_pair_template = """
I have a client requirement document for a software project and need your assistance in extracting detailed information. Please address the following queries based on the provided user requirement document.Please thoroughly analyze the entire document to ensure you capture all relevant details. Provide comprehensive and detailed answers to each query based on the given context. If the answer is not found in the provided document, state "Not found in the provided document."


Queries:
```{user_queries}```

User Requirement Document:
```{requirement_document}```


Use this format instruction for its output:
{format_instructions}
"""

phase_template = """
So i have information regarding a software application i want to implement it. I want you to take context from the information i have provided that make phases for its implementation
You need to add as much descrpition you find from the context in each phase.
How need to act:
1. First you need to identify what kind of app it is is it web app, mobile app , autmation application, AI project or Data engineering project
2. Bawsed on what kind of app it is you need to see what kind of phases will be required by it.
3. Feel free toignore a phase if it is not reuired for app
4. For each phase you need to add as mush description as possible for that phase to be implemented

Following are the main features which are generally required for a software development:
```{project_phases}```

Following are the queries and their answers from the user requirement document:
```{user_queries}```

Use this format instruction for its output:
{format_instructions}
"""

paraphrase_template = """
Paraphrase the following user requirement document to improve readability while retaining all important information:

User Requirement Document:
```{requirement_document}```
"""
