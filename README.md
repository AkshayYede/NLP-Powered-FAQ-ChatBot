# **NLP-Powered FAQ Chatbot** 🚀  

## **Overview**  
This project is an **AI-driven FAQ chatbot** built using **Natural Language Processing (NLP)** techniques. The chatbot allows users to either select predefined questions or type their own queries to receive relevant responses. By leveraging **Sentence-BERT embeddings** and **cosine similarity**, the chatbot can accurately retrieve answers based on semantic meaning rather than just keyword matching.  

## **Key Features**  
🔹 **NLP-Based Semantic Search** – Uses Sentence-BERT for understanding user queries.  
🔹 **Dynamic Question Selection** – Users can pick questions from a list, which dynamically adjusts after selection.  
🔹 **Typewriter-Style Responses** – Answers appear gradually for a smooth user experience.  
🔹 **Interactive UI** – Designed for desktop with an engaging and user-friendly interface.  
🔹 **Flask Backend** – Manages queries and processes responses efficiently.  

## **Technology Stack**  
✨ **Natural Language Processing (NLP)** – Sentence-BERT (`paraphrase-MiniLM-L6-v2`)  
✨ **Machine Learning** – Cosine similarity for question-answer matching  
✨ **Backend** – Flask for API and application logic  
✨ **Frontend** – HTML, CSS, JavaScript, and jQuery for an interactive UI  
✨ **Data Handling** – CSV file storing FAQ data  

## **How It Works**  
1️⃣ Users either type a query or select from predefined FAQ options.  
2️⃣ The chatbot converts the user query into an **embedding** using **Sentence-BERT**.  
3️⃣ It calculates **cosine similarity** between the user query and existing FAQ questions.  
4️⃣ The best-matching answer is retrieved and displayed in a **typewriter-style effect**.  
5️⃣ Users cannot select another question until the response is fully displayed, ensuring a smooth experience.  

## **Use Cases**  
✅ **Customer Support Automation** – Instantly answer common customer queries.  
✅ **Knowledge Base Search** – Enhance internal documentation search for teams.  
✅ **Educational Chatbots** – Provide instant answers to frequently asked academic questions.  

## **Future Enhancements**  
🔹 **Database Integration** – Switch from CSV to a database like PostgreSQL or Firebase.  
🔹 **Voice Input Support** – Enable users to ask questions using speech-to-text.  
🔹 **Improved AI Model** – Experiment with larger transformer models for better accuracy.  
🔹 **Cloud Deployment** – Host the chatbot online for real-world accessibility.  

This project is a step towards making **FAQ systems smarter and more interactive** using **NLP**. 🚀
