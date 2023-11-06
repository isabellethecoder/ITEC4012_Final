# ITEC4012_Final

https://github.com/isabellethecoder/ITEC4012_Final.git

Ok so this was definitely an experience. So I will not lie I had a very hard time setting up the project, I reviewed the in-class demo that was made with the todoapp and once I felt confident I started my own project. I followed the instructions but kept getting errors. I attempted again so I decided to just base it on the original todo demo if you're wondering why the naming convention had nothing to do with the app.

Once the base was made, I tackled the search function since that is the main feature. For some reason, this was the most difficult thing I could possibly do.

https://www.youtube.com/watch?v=AGtae4L5BbI&ab_channel=Codemy.com
I used this as a reference for the base

I new how to make the form but it was submitting it that was the bigger issue. Once I got the form in html I made a SearchBar model that took the user input and stored it as a string. Next I made SearchQuery which stores the search as a string.

then in views, I made the search_results which took the user's input with GET and stored it. The search_tv_shows is for the APIS, I used https://www.tvmaze.com/api?ref=apilist.fun#show-search

The search_tv_shows is responsible for connecting the TV API by searching up the user's query. If the response code is 200 the view processes the json data and extracts the information about the tv show. I had a very hard time with this. It was showing that the response was 200 but would display you searched for: blah blah blah and no results found. I was able to fix this by saving the search query and then making the API request so one set of results is returned.

I'm feeling more confident then I was at the start. I'm aware that the backend code isn't entirely completed but i think I have the base necessary to finish. All I have to do is make the API endpoint show information which is possible extract holiday episodes and make the info on the holiday chosen in the drop down menu storable.


ALSO IDK WHY IT SAYS THE MAIN PLS OPEN finalAssignment01.2