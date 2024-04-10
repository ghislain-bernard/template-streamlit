#!/usr/bin/env python3
#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import string
import sys
import timeit
import types

import emoji # https://carpedm20.github.io/emoji/

import PIL.Image as pillow

import streamlit as st

#----------------------------------------------------------------------------------------------------------------------#

import module.blue
import module.white
import module.red

#----------------------------------------------------------------------------------------------------------------------#

def main():

  if 'verbose' not in st.session_state:
    st.session_state['verbose'] = False

  ########################

  st.set_page_config(layout='wide', page_title='Template')

  with open('style.css', encoding='utf-8') as file:
    st.markdown('<style>' + file.read() + '</style>', unsafe_allow_html=True)

  ########################

  st.title('Template', 'title')
  st.image(pillow.open('streamlit.webp'))

  st.button('Rerun')

  ########################

  if st.sidebar.button(emoji.emojize(':speech_balloon:')):
    st.session_state['verbose'] = not st.session_state['verbose']

  ########################

  verbose: bool = st.session_state['verbose']
  if verbose:
    st.info('verbose = {}'.format(verbose), icon=emoji.emojize(':speech_balloon:'))

  ########################

  timer: float = timeit.default_timer()

  ########################

  options: dict[str | None, types.ModuleType] = {
    None: sys.modules[__name__],
    'blue': module.blue,
    'white': module.white,
    'red': module.red
  }

  option: str | None = st.sidebar.selectbox('module', [option for option in options if option is not None],
                                            index=None,
                                            key='module',
                                            placeholder='none')

  ########################

  st.sidebar.markdown('---')
  st.sidebar.markdown('### {}'.format(emoji.emojize(':gear:')))

  st.sidebar.number_input('number', 1, 9, 5, key='number')
  st.sidebar.multiselect('letters', tuple(string.ascii_uppercase), key='letters', placeholder='none')

  options[option].run(verbose)

  ########################

  st.markdown('---')

  st.markdown('#### {} Dependancy'.format(emoji.emojize(':x-ray:')))
  st.table({'module': ['python', 'streamlit'], 'version': [sys.version.split(maxsplit=1)[0], st.__version__]})

  ########################

  st.markdown('---')

  st.markdown('##### -')
  st.markdown('##### {} in {:.3f} second(s)'.format(emoji.emojize(':rocket:'), timeit.default_timer() - timer))

  ########################

  st.balloons()

#----------------------------------------------------------------------------------------------------------------------#

def run(verbose: bool):

  st.markdown('---')

  number: int = st.session_state['number']
  if verbose:
    st.info('number = {}'.format(number), icon=emoji.emojize(':speech_balloon:'))

  message: str = emoji.emojize(':Japanese_application_button:') * number
  if verbose:
    st.info('message = "{}"'.format(message), icon=emoji.emojize(':speech_balloon:'))

  st.markdown('# {}'.format(message))

  #######################

  letters: list[str] = st.session_state['letters']
  if verbose:
    st.info('letters = {}'.format(letters), icon=emoji.emojize(':speech_balloon:'))

  if letters:
    st.markdown('# :rainbow[{}]'.format('-'.join(letters)))

#----------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
  main()

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
