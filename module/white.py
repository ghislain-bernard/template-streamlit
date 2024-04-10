#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import emoji

import streamlit as st

#----------------------------------------------------------------------------------------------------------------------#

def run(verbose: bool):

  st.markdown('---')

  number: int = st.session_state['number']
  if verbose:
    st.info('number = {}'.format(number), icon=emoji.emojize(':speech_balloon:'))

  message: str = emoji.emojize(':white_large_square:') * number
  if verbose:
    st.info('message = "{}"'.format(message), icon=emoji.emojize(':speech_balloon:'))

  st.markdown('# {}'.format(message))

  #######################

  letters: list[str] = st.session_state['letters']
  if verbose:
    st.info('letters = {}'.format(letters), icon=emoji.emojize(':speech_balloon:'))

  if letters:
    st.markdown('# {}'.format('-'.join(letters)))

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
