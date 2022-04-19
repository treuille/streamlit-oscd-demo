# Streamlit OSDC Demo

This is a demo of how to use Streamlit. It is modeled on the [Udacity Self-driving Car
demo](github.com/streamlit/demo-self-driving).

# Outline of the Demo

## Step 1: Installing Streamlit

```sh
pipenv install
```

## Step 2: Testing your install

```sh
pipenv run streamlit hello
```

Or alternatively:

```sh
pipenv shell
streamlit hello
```


## Step: Let's make a simple hello world program

```python
num_hellos = st.slider("How many hellos", min_value=1, max_value=10)
for i in range(num_hellos):
    st.write(i, "Hello, world!!")
```
