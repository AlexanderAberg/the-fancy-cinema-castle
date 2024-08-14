

### Validator Testing 

- HTML
 - Official validator [W3C validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Falexanderaberg.github.io%2FDifferent-Coloured-Tea%2Findex.html) was used for all HTML validation.
  -  No errors were returned.
<img src="assets/images/testing/validator-html-home.png" alt='Validator Home html'>

 -  No errors were returned.
<img src="assets/images/testing/validator-html-about.png" alt='Validator About html'>

 -  No errors were returned.
<img src="assets/images/testing/validator-html-bookings.png" alt='Validator Bookings html'>

  -  4 errors were returned related to Django code, so it's not related to my code.
<img src="assets/images/testing/validator-html-signup.png" alt='Validator Signup html'>

-  No errors were returned.
<img src="assets/images/testing/validator-html-login.png" alt='Validator Login html'>

-  No errors were returned.
<img src="assets/images/testing/validator-html-logout.png" alt='Validator Logout html'>

  
- CSS
  -  No problems, 3 warnings related to fonts and browsers [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
<img src="assets/images/testing/validator-css.png" alt='Validator css'>


- JS
  - No errors was returned for JS, but 41 warnings, in the same style about ES6, also warning for undefined variable bootstrap and three unused variables on first 3 rows, 
  but if I try change or remove and of the mentioned variables my bookings page stops working as it is supposed to, either by not remembering information on edit or by copying bookings during edit,
   even if there is already 2 bookings [(Jigsaw) validator](https://jshint.com/).
<img src="assets/images/testing/validator-js.png" alt='Validator js'>


- Python
 - Official Python Validator [PEP8 Python Validator](https://pep8ci.herokuapp.com/#)

- fancy_cinema_castle directory
  - No errors were returned, but 5 lines being too long, which you will clearly see in the image why.
<img src="assets/images/testing/validator-js-settings.png" alt='Validator Settings Python'>
 - No errors were returned, but 5 lines being too long, which you will clearly see in the image why.
<img src="assets/images/testing/validator-js-fancy-urls.png" alt='Validator Fancy-URLS Python'>


### Quality Score through Google Devtools Lighthouse

- Lighthouse testing on Chrome Incognito to prevent cookies and background cache to slow down.
- Bookings is checked when both a bookings is made and the booking form is still there.

<img src="assets/images/lighthouse/lighthouse-home-phone.png" alt="Lighthouse Home Phone">
<img src="assets/images/lighthouse/lighthouse-home-desktop.png" alt="Lighthouse Home Desktop">
<img src="assets/images/lighthouse/lighthouse-about-phone.png" alt="Lighthouse About Phone">
<img src="assets/images/lighthouse/lighthouse-about-desktop.png" alt="Lighthouse About Desktop">
<img src="assets/images/lighthouse/lighthouse-bookings-phone.png" alt="Lighthouse Bookings Phone">
<img src="assets/images/lighthouse/lighthouse-bookings-desktop.png" alt="Lighthouse Bookings Desktop">
<img src="assets/images/lighthouse/lighthouse-register-phone.png" alt="Lighthouse Register Phone">
<img src="assets/images/lighthouse/lighthouse-register-desktop.png" alt="Lighthouse Register Desktop">
<img src="assets/images/lighthouse/lighthouse-login-phone.png" alt="Lighthouse Login Phone">
<img src="assets/images/lighthouse/lighthouse-login-desktop.png" alt="Lighthouse Login Desktop">
<img src="assets/images/lighthouse/lighthouse-logout-phone.png" alt="Lighthouse Logout Phone">
<img src="assets/images/lighthouse/lighthouse-logout-desktop.png" alt="Lighthouse Logout Desktop">
