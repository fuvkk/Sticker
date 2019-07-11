import logging

from telegram.ext import ConversationHandler, CallbackContext
from telegram import Update, ChatAction

from ..utils import decorators
from bot import markups as rm
from bot import strings as s

logger = logging.getLogger(__name__)


@decorators.action(ChatAction.TYPING)
@decorators.restricted
@decorators.failwithmessage
def cancel_command(update: Update, context: CallbackContext):
    logger.info('%s command', update.message.text)

    update.message.reply_text(s.CANCEL, reply_markup=rm.HIDE)

    # remove temporary data
    context.user_data.pop('pack', None)
    
    return ConversationHandler.END
