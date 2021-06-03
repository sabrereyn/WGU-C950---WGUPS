# WGU C950 WGUPS Project Assessment
 
Scenario:
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.


Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

Notes:
This project was done using the greedy algorithm and a hybrid of manual and automated loading of packages. The total mileage ends at around 123 miles and all packages were delivered well before noon.

Things that could be used to improve upon this project is the loading of packages. If searching for the most optimal solution, the greedy algorithm won't provide it as it provides the most optimal solution step by step. With that being said, this meets all requirements and provides a solution to delivering 40 packages.
