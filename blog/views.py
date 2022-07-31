from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "Indy-and-Henry-in-an-airplane.png",
        "author": "Stefanos Pizanias",
        "date": date(2022, 7, 22),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when flying an airplane!",
        "content": """    
        Professor Henry Jones: [accidentally shoots their own plane with the machine gun]

        Indiana Jones: Dad, are we hit?

        Professor Henry Jones: More or less. Son, I'm sorry. They got us.

        """
    },
    {
        "slug": "programming-is-fun",
        "image": "indiana-jones-et-la-dern-ii02-g.jpg",
        "author": "Stefanos Pizanias",
        "date": date(2022, 5, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code?",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "Holy-Grail.jpg",
        "author": "Stefanos Pizanias",
        "date": date(2022, 6, 5),
        "title": "Python At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          [singing] 
          We're knights of the Round Table, we dance whene'er we're able. 
          We do routines and chorus scenes with footwork impec-cable, 
          We dine well here in Camelot, we eat ham and jam and Spam a lot. 
          / We're knights of the Round Table, our shows are for-mi-dable. But many times we're given rhymes that are 
          quite un-sing-able, We're opera mad in Camelot, we sing from the diaphragm a lot. 
          / In war we're tough and able, Quite in-de-fa-ti-gable. Between our quests we sequin vests 
          and impersonate Clark Gable 
          / It's a busy life in Camelot
        """
    }
]


def get_date(post):
    return post.get("date")

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
