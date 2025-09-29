from flask import Flask, redirect, render_template, url_for
from static.texts.texts import another_needle, first_stitch

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('staticpage',pagename='home'))

@app.route('/research')
def research():
    return redirect(url_for('staticpage',pagename='research'))

def imgUrl(name):
    return url_for('static',filename='imgs/'+name+".jpg")

def textUrl(name):
    print("looking for: "+url_for('static',filename='texts/'+name+".txt"))
    return url_for('static',filename='texts/'+name+".txt")

@app.route('/staticpage/<pagename>')
def staticpage(pagename):
    title = "Will's "+pagename
    if pagename=="home":
        currentthemeimage = imgUrl('forest_pool')
        return render_template('home.html',
            title=title,
            currentthemeimage=currentthemeimage)
    elif pagename=="research":
        currentthemeimage = imgUrl('rainy_monorail')
        return render_template('research.html',
            title=title,
            currentthemeimage=currentthemeimage)
    elif pagename=="explainers":
        return redirect(url_for('explainers',explainer="home"))
    elif pagename=="contact":
        currentthemeimage = ""
        return render_template('contact.html',
            title=title,
            currentthemeimage=currentthemeimage)
    elif pagename=="writing":
        return redirect(url_for('wjtreader',textname="HOME"))
    elif pagename=="library":
        return redirect(url_for('library',qtype="home"))
    else:
        return render_template('fourhundredandfour.html',
            title=title)

@app.route('/explainers/<explainer>')
def explainers(explainer):
    title = "Will's explainers"
    currentthemeimage = imgUrl('steam_tank')
    if explainer == "home":
        return render_template('explainers.html',
            title=title,
            currentthemeimage=currentthemeimage)
    else:
        return "<p>Explainer not found.</p>"


@app.route('/library/<qtype>')
def library(qtype): # here qtype will determine the type of library query made
    title = "Will's library"
    currentthemeimage = imgUrl('mysterious_cat')
    if qtype == "home":
        return render_template('libhome.html',
            title=title,
            currentthemeimage=currentthemeimage)
    else:
        return "<p>Alas, the library query type was not recognised.</p>"



@app.route('/wjtreader/<textname>')
def wjtreader(textname): # here is the name of the py file that contains the text text
    if textname == "HOME":
        title = "Writing"
        currentthemeimage = imgUrl('lathanorin')
        return render_template('writing.html',
            title=title,
            currentthemeimage=currentthemeimage)
    if textname == "another_needle":
        title = "novella #3: Another Needle - April 2024"
        return render_template('wjtreader.html',
            title=title,
            text=another_needle)
    if textname == "first_stitch":
        title = "Last Stitch - December 2024"
        return render_template('wjtreader.html',
            title=title,
            text=first_stitch)
    else:
        return "<p>Alas, text with that name could not be found.</p>"



if __name__ == "__main__":
   app.run(host='0.0.0.0')
