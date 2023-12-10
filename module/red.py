#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#

import emoji

import streamlit as st

#----------------------------------------------------------------------------------------------------------------------#

def run(verbose: bool):

  st.markdown('---')

  number: int = st.session_state['number']
  if verbose:
    st.info('number = {}'.format(number), icon=emoji.emojize(':speech_balloon:'))

  message: str = emoji.emojize(':red_square:') * number
  if verbose:
    st.info('message = "{}"'.format(message), icon=emoji.emojize(':speech_balloon:'))

  st.markdown('# {}'.format(message))

#--------------------------------------------- ghislain.bernard@gmail.com ---------------------------------------------#
