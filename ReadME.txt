Final Assignment
Isabelle Legault
101 200 960

The website starts at the home screen. The home screen has an explore page with different holidays and shows to explore. There are 5 shows per category. I was planning to add more and make it a carousel, but the images were making it extremely long to load. So, I cut down the shows to 5 per category instead of 10. I like this feature because if I wanted to, I could go in and hard code specific TV shows. This way, if this website were to be published, I could change the explore page and keep it fresh for the users. In this code, I didn't do that; instead, I made it search the API's database for shows that contain the category keyword, like Christmas.

Another feature that appears is the navigation bar with the logo and search bar. The navigation bar is fixed so it overlays over the website, making the navigation always available to the user. The logo is clickable and, no matter what page you're on, will always bring you back to the home page. There is also the search bar. The search bar allows the user to search the API's database for a show. The results will show all shows with the keyword in the search or similar words.

If you click one of the shows on the home page, it will bring you to the showIndex page. I will get into that page in a moment.

The second main page is the search results. So when you search for a show, it will bring you to the result page. Technically, this is the same page; in the future, I would have added a new HTML file for this page. As mentioned, it shows all the shows in the API's database that correspond to the keyword and shows with similar titles. When you click the show you're looking for, it brings up the information.

In the episode information page, it lists the available holiday episodes. I made it so that when it loads, it searches all the episodes' summaries for keywords. The keywords are a list of holidays:

'Christmas': ["Christmas", "Holiday"],
'Halloween': ["Halloween"],
'Hanukkah': ["Hanukkah"],
'Thanksgiving': ["Thanksgiving"],
'Easter': ["Easter"],
'New Year': ["New Year", "New Year's Eve", "New Year's Day"],
'Diwali': ["Diwali"],
'Valentine's Day': ["Valentine's Day", "Valentine Day", "Valentines Day"],
'Independence Day': ["Independence Day"],
'Labor Day': ["Labor Day"],
'Cultural Festivals': ["Carnival", "Oktoberfest", "Lunar New Year"],
'St-Patric's Day': ["St-Patric.", "St. Patty", "St. Patric"]


If it finds one of these keywords, it will create a category with the episode listed in the category. This way, if there are no holiday episodes, it won't be full of empty categories. Or if there is only one holiday category, only that will be shown, once again not leaving a list of empty categories. This will make it look cleaner and easier to read.

I did not add a data base. I saw you're comment on the backend but I didn't really know how to implement a databse. I was considering to do a history, but I cut my losses. Also I had anticipated adding a lot more images for example all the episode images but it was taking WAY to long to load in the pages.