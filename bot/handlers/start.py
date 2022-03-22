import logging
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyrogram.types import (
    Message,
    Voice,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)

# noinspection PyPackageRequirements
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    ConversationHandler
)
# noinspection PyPackageRequirements
from telegram import (
    ChatAction,
    Update
)

from bot import stickersbot
from bot.utils import decorators
from bot.strings import Strings
from config import config

logger = logging.getLogger(__name__)


@decorators.action(ChatAction.TYPING)
@decorators.restricted
@decorators.failwithmessage
def on_help_command(update: Update, context: CallbackContext):
    logger.info('/help')

    update.message.reply_html(Strings.HELP_MESSAGE.format(context.bot.username))

    return ConversationHandler.END


@decorators.action(ChatAction.TYPING)
@decorators.restricted
@decorators.failwithmessage
def on_start_command(update: Update, _):
    logger.info('/start')

    start_message = Strings.START_MESSAGE
    if config.bot.sourcecode:
        start_message = '{}\n🛠 <a href="{}">source code</a>'.format(start_message, config.bot.sourcecode)
    if config.bot.get('channel', None):
        start_message = '{}\n📣 <a href="https://t.me/{}">announcements channel</a>'.format(start_message, config.bot.channel)

    update.message.reply_html(start_message)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "About", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "Basic Guide", callback_data="cbguide")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        )
   

    return ConversationHandler.END


stickersbot.add_handler(CommandHandler('help', on_help_command))
stickersbot.add_handler(CommandHandler('start', on_start_command))
