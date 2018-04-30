### Peer Production Project Experience Report  

&nbsp;

#### Original Expectations and Problems

Originally, I intended to implement, push, and merge a bug fix to one of the issues listed on GitHub to the Atom GitHub repo. Unfortunately, however, my contributions did not go according to plan. After forking the Atom Github repo and cloning the repo onto my computer, I began following through the documentation on GitHub as to how to build the Atom code for development. I was able to locate the build script inside my cloned repo; however, upon running the build script, many errors were thrown. Initially, I assumed that these errors were due to my version of NodeJS and NPM, so I downloaded the recommended versions of NodeJS and NPM and ran the script again. Yet, the same errors were thrown by the build script. After hours of attempting to identify the locus of my errors, I decided to switch the scope of my contribution to the Atom project from implementing a bug fix to designing and implementing a new UI/syntax theme for Atom.

&nbsp;

#### Atom UI and Syntax Themes

Because Atom is a fully open source and customizable/configurable text editor, individuals in the Atom community can contribute custom themes to Atom for other users to pull and use. Themes dictate the style and look of the text editor and are broken up into two different types: syntax themes (themes that dictate the styling of the code written in the editor) and UI themes (themes that dictate the styling of the Atom interface). 

&nbsp;

#### Contributions

I began my development by forking an Atom syntax template repo and an Atom UI template repo from GitHub. I cloned these repos onto my computer, opened up Atom, set Atom up to run in development mode (a mode which allows developers to see changes applied to Atom in real-time), and began tweaking colors, fonts, and spacings. Since the Atom interface is based in HTML, the themes are based in a CSS derivation called LESS. I was able to make contributions to color variables, font variables, and style variables in LESS to change the look and feel of Atom. 

&nbsp;

#### Publishing Contributions

Once I was satisfied with the syntax and UI themes that I had developed, I published my styles to Atom to be publicly accessible. I pushed my code to GitHub, added the link to the GitHub repo to the syntax and UI package.json files, and ran ‘apm publish’ in a terminal to publish my code to the Atom style repositories. Anyone can contribute a theme for Atom. There is no review process required to have styles accessible for others to use; as long as the developer has linked their GitHub account with Atom.io, they can quickly and easily publish any package, plugin, or theme to the Atom servers. My themes are now listed on the Atom site - [Simple UI](https://atom.io/packages/simple-ui) and [Simple Syntax](https://atom.io/packages/simple-syntax) - and can be downloaded and used by any Atom user. Overall, my experience creating a style for Atom was simple and easy to do. It matched my expectations as to how users of contribute to Atom by making additions and tweaks to the program. 
