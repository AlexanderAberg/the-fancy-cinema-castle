# The Fancy Cinema Castle
- The Fancy Cinema Castle is a page where you can book auditoriums for viewing movies or play games.
- It is an esclusive experience and compared to a normal cinema you book the whole auditorium and not just a couple of seats.
- You will be able to see what is on offer in a user friendly site.
- Link to the live version of the project can be found here: https://the-fancy-cinema-castle-7eb7ea1dedc6.herokuapp.com/
- Link to the GitHub page here: https://github.com/AlexanderAberg/the-fancy-cinema-castle 

<img src="assets/images/amiresponsive.png" alt="Responsive Screens">


# UX
### Visitor Goals
The expected visitor is:
- Visitors that wants to watch a movie or play games with friends.
- Visitors that wants to go to the cinema without having random people in the auditorium but instead people they choose.
- Visitors that wants to have a great time with friends and family.

Visitors goals are:
- Be able to book an auditorium according to their wishes.
- See what is on offer.
- Read about the concept.

How The Fancy Cinema Castle fills the needs:
- You can get information about different auditoriums.
- You can read about the concept.
- You can register to book the aditorium, which you later can edit and cancel if your circumstances changes.


### Business Goals
The Business Goals are:
- To give a superior experience compared to a normal cinema.
- To also offer you to play video games on a cutting edge cinema auditorium.
- To give you a great time.

### User Stories
1. As a Site Creator I can deploy the project so that I can make it accessible for the user.
2. As a Site User I can register an account so that I can book an auditorium.
3. As a Site User I can use a navigation bar so that I can in an easy way find what I am looking for.
4. As a Site User I can navigate through with all links and buttons so that I can the full use of the site.
5. As a Site User I can get info from the footer so that I can get contact information and address of the company.
6. As a Site User I can create a booking so that I can be able to book an auditorium.
7. As a Site User I can see relevant icons on the site so that I can get a better UX.
8. As a Site User I can get more info about the specific auditorums so that I can understand what is on offer.
9. As a Site User I can use the booking manager so that I can make a correct booking.
10. As a Site User I can get information about the concepts and book so that I can get an understanding of the business.
11. As a Site User I can look at a carousel on home page so that I can see my auditorium options.
12. As a Site User I can see pictures so that I can see what it looks like.
13. As a Site User I can edit and cancel my booking so that I can adjust to my wants and needs.
14. As a Site Admin I can see other peoples bookings so that I can prepare the staff.
15. As a Site User I can edit my profile so that I can have my info up to date.

### Existing Features

- __Header__
  - Header has a menu with a nav bar or text on bigger screens and a logo of a castle with a ghost, which you can also see on the favicon.

<img src="assets/images/header.png" alt="Header">

- __Navigation Bar__

  - The navigation bar can be found on all pages and is fully responsive, it will turn between a bar or buttons depending on the size of the screen.

<img src="assets/images/navbar.png" alt="Nav bar">

- __The landing page__

  - The landing page or "Home" has a carousel with pictures and some information about the concept.
  - The carousel has links to bookings, a subheader and an AI created image related to the auditorium on each side, the image is castle themed while fitting the genre.

<img src="assets/images/landingpage.png" alt="Landing Page">

- __The background picture__

  - The background picture can be seen on all pages, is AI generated and is a castle with a cinema auditorium outside, the dark colours is to make it look good on all screen sizes.

<img src="assets/images/background.png" alt="Background">

- __About page__

  - The about page has information about each auditorium and links to bookings. 

<img src="assets/images/about.png" alt="About page">

- __Bookings__

  - The bookings page has the bookingmanager and the bookings.
  - The buttons will be coloured according to if it increases or decreases your risk.

  <img src="assets/images/bookings.png" alt="Bookings page">

- __Booking Manager__

  - The Team page has information about the team, with pictures, short info and links to LinkedIn and GitHub.

<img src="assets/images/booking-manager.png" alt="Booking Manager">

- __The Footer__ 

  - The footer has contact information and Copyright info.

<img src="assets/images/footer.png" alt="Footer">


### Thoughts behind my choices

- I wanted to make an exclusive cinema experience with video games that I would want to visit.
- The dark colours shows excitement and does fit with a dark cinema room, also fit with castle theme.
- The theme and pictures are very castle related, I did choose the name because it is fancy and what is more fancy than a castle?
- I had to cut down on some ideas even if the project to 90% went my way, I did not want to make it to big because of time limits.


### Agile

- I planned pretty wide user stories to make it possible to change plans.
- I have cut down on my plans which you can see on Wireframes and the flowchart.
- The project is adjusted so future implementations is possible.


### Kanban

- Worked in a Kanban board on GitHub to see where we are with our features in the project.
- https://github.com/users/AlexanderAberg/projects/4/views/1

<img src="assets/images/user-stories.png" alt="User Stories Kanban">


### Features Left to Implement

- in the booking manager it should be possible to choose the numbers of options you want or not at all, you should also have a calendar for date/time.
- The booking manager should have a different design for choices like calendar I mentioned, but also radio buttons for sessions and checkboxes for options.
- Should in the future be possible with only 3 time frames per auditorium and day, you should get an error if it is already booked.
- Will be possible with editing your profile and add extra information.


### Testing 

- See separate file for testing information here: <a href="testings/">


### Validator Testing 

- HTML
  -  [W3C validator](https://validator.w3.org/nu/?).
- CSS
  -  2 issues and 1 warning [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?) 
- JS
  - No errors was returned for JS, but 41 warnings, in the same style about ES6 [(Jigsaw) validator](https://jshint.com/).

<img src="assets/images/validator-html.png" alt='Validator html'>
<img src="assets/images/validator-css.png" alt='Validator css'>
<img src="assets/images/validator-js.png" alt='Validator js'>


### Unfixed and fixed Bugs

- There is a bug that you don't get information about booking not possible when you for example don't have a correct date or amount of people, but the form works in a correct way so the auditorium won't get booked,
you can also see that it isn't booked because the booking message isn't shown.
- I had a hard time making the forms for register, log in and log out show up while at the same time letting the background being placed correctly.
I solved it by removing some classes and by changing the z-index for the background to be behind content, but it wasn't enough for the forms, so I also had to create a new form class with an absolute position.
This took some time and a lot of try and error, trying to find resources mainly on the bootstrap website, checking slack and then contacting Sarah on Tutor Support that suggested looking at the position of the specific forms and to create a class related to it.


### Quality Score through Google Devtools Lighthouse

- Lighthouse testing on Chrome Incognito to prevent cookies and background cache to slow down.

<img src="assets/images/lighthouse-home-phone.png" alt="Lighthouse Home Phone">
<img src="assets/images/lighthouse-home-desktop.png" alt="Lighthouse Home Desktop">
<img src="assets/images/lighthouse-std-phone.png" alt="Lighthouse STD Phone">
<img src="assets/images/lighthouse-std-desktop.png" alt="Lighthouse STD Desktop">
<img src="assets/images/lighthouse-questionnaire-phone.png" alt="Lighthouse Questionnaire Phone">
<img src="assets/images/lighthouse-questionnaire-desktop.png" alt="Lighthouse Questionnaire Desktop">
<img src="assets/images/lighthouse-team-phone.png" alt="Lighthouse Team Phone">
<img src="assets/images/lighthouse-team-desktop.png" alt="Lighthouse Team Desktop">

### Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 
  - You can either copy the link for Code or Open in a new repository or see the live version under Deployment to the right under github-pages.
  - In GitHub you can open every seperate file and see the folder structure.
  - It is possible to check the commit history in github-pages under Deployment to the right.
- What to do in Heroku:
  - Create a new app in Heroku, name it and choose your region before pushing button to create app.
  - In the next page press settings, scroll down to Config Vars and push the button, here you add CLUuDINARY_URL, DATABASE_URL and SECRET_KEY with all the relevant keys related to your cloudinary account, database and secret key.
  - Now you go up to switch to Deploy in the tab and here you press the GitHub icon with the GitHub text to connect to GitHub and after that press Connect to GitHub button below.
  - You will get a name choice where you choose your GitHub and search for the correct respository and then press connect.
  - You will now be able to press Enable Automatic Deploys to make changes come automatically or do a manual deploy through the button Deploy Branch which will give you access already after about 30 seconds,
  after the 30 seconds give or take depending on your internet speed and computer you can press view and now you have access to use the app.
  - Now you will also be able to find the deployment in GitHub including all commits that was done after the deployment

  - Link to the live version of the project can be found here: - https://the-fancy-cinema-castle-7eb7ea1dedc6.herokuapp.com and to the GitHub page here: https://github.com/AlexanderAberg/the-fancy-cinema-castle


### Credits 

- Help and support from tutors and my mentor Rory Patrick.


### Content 

- I made up the content and my inspiration is just normal life.


### Media

- Used Freepik AI to create the cinema castle image and the images in the carousel, here is link to the tool: https://www.freepik.com/pikaso/ai-image-generator.
- Icon and Favicon from https://www.freepik.com/icon/haunted-house_950727 
- Responsive image from https://ui.dev/amiresponsive
- Colour generator from https://coolors.co/ 



### Wireframe

- Used Balsamiq for Wireframe

<img src="assets/images/wireframe-desktop-home.png" alt="Wireframe on Desktop for Home page">
<img src="assets/images/wireframe-desktop-about.png" alt="Wireframe on Desktop for About page">
<img src="assets/images/wireframe-desktop-bookings.png" alt="Wireframe on Desktop for Bookings page">
<br>
<img src="assets/images/wireframe-tablet-home.png" alt="Wireframe on Tablet for Home page">
<img src="assets/images/wireframe-tablet-about.png" alt="Wireframe on Tablet for About page">
<img src="assets/images/wireframe-tablet-bookings.png" alt="Wireframe on Tablet for Bookings page">
<br>
<img src="assets/images/wireframe-phone.png" alt="Wireframe on Phone for all 3 pages">


### Flowchart

- Flowchart made with Lucid Charts.

<img src="assets/images/flowchart.png" alt="Lucid Charts Flowchart">

### Technologies Used

- HTML - For how the website with the pages is built and planned 
- CSS - For styling
- JS - For edit and delete on form
- Python - For backend
- Django - As Python framework
- Bootstrap - For styling
- Images  - Freepik including their AI
- Fonts - From Google Fonts
- Icons - From Fontawesome 
- Wireframe - From Balsamiq
- Flowchart - Lucid Charts
- Favicons - Icon from Freepik and generated with Favicon.io
- Responsive mockup - Generated at  ui.dev/amiresponsive
- Colour generator mockup - Generated at coolors.co
- Google Devtools - to check responsiveness and to check Lighthouse for Accessibility
- GitHub - for storing the project and to get to the deployed version, also for User Stories with Kanban
- Heroku - For deploying the project
- Project Development - GitHub and Visual Studios
- Markup - For this README and User Stories



### Colours

- Colours that would be smooth while standing out from the images and bootstrap.
- The image doesn't include bootstrap colours, the most used bootstrap colour is dark with light buttons and lines.

<img src="assets/images/colours.png" alt="Colours">