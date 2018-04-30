#Experience Report
Yu Zhang


### Overview of the Project

The project I am working on is the samples of Digital Public Library of America(DPLA). as I stated in community identification, it is a peer production project and worth studying. This library with a vast amount of information is a great storehouse for researchers to find information they need. And they have developed a full set of APIs to meet the need of retrieving information. They also collect samples of the APIs for various programming languages. So my goal is contributing a sample and push it to the sample pool.

### Procedure of Implementation 

- Studying how it works

In the beginning, I found the way how DPLA collects data is rather interesting. There are a lot of Hubs throughout the country, such as Michigan DPLA Service Hub, or some large libraries, Hubs provide data for DPLA. Hubs send data directly to dataProviders, and dataProviders will filter unuseful data, and encapsulate useful data into items. Then there are providers who collect items from their dataProviders. So each item stores many terms, such as which provider and dataProvider it comes from, the URI where its content comes form, and the date when it is collected.

There are some built-in APIs to help developers retrieve items, query by content in items, and fetch a list of a specific term. So after learning the process of how DPLA collects items and these APIs, I decided to write a program about how to retrieve all the providers and dataProviders. After reading the samples I thought it would be a good idea.

- Contributing 

After discussing with the administrator about how this procedure works, I started working on the project. Firstly, I went through the API document and Metadata Application Profile, and figure out what information each item contains as metadata. And then I tried to find which interface I should use, and studied what workflow and algorithm should be in my code, and how providers relate to dataProviders. Finally when I implemented the function and debugged, I put all the sample in one package and run them together, to see whether there is a conflict or not.

After implementing the code, I sent a pull request and have been keeping in touch with the administrator. I have also talked with some of contributors and they said my sample was qualified.

### Conclusion

I feel fulfilled after participating in this peer production project, as I have talked with many excellent developers, and have completed a part of this great project. I realized one of the meaning of peer production project is collecting ideas of brilliant minds into a project.


