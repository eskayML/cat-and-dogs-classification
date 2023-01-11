# cat-and-dogs-classification

View [Live on Spaces](https://huggingface.co/spaces/eskayML/cat-and-dog-classifier)

A machine learning project for classifying images of cats and dogs
> Curated a dataset containing 25000 images of cats and dogs 

## STEPS  I TOOK BUILDING THE APPLICATION:
<hr>
- I built a model using convnets architecture and applied techniques like data augmentation and transfer learning 
<br>
- I then fitted the model to a larger portion of the data (training set). Note that I used a smaller portion(about 20%) for testing/validation 
<br>
- Checked the performance on the test data
<br>
- I built an interface for the model using streamlit 
- Live deployment to hugging face spaces

## HOW TO USE THE APP LOCALLY

```console
$ git clone https://github.com/eskayML/cat-and-dogs-classification

```
```console
$ cd cat-and-dogs-classification

```

```console
$ pip install -r requirements.txt

```
Install the dependencies using the command above and then run 

```console
$ streamlit run main.py

```

