#   Copyright 2019 - 2020 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import requests
from userbot import bot
from telethon import events
from var import Var
from pathlib import Path
from userbot.uniborgConfig import Config
from userbot import LOAD_PLUG
from userbot import CMD_LIST
import re
import logging
import inspect

def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    if 1 == 0:
        return print("stupidity at its best")
    else:
        pattern = args.get("pattern", None)
        allow_sudo = args.get("allow_sudo", None)
        allow_edited_updates = args.get('allow_edited_updates', False)
        args["incoming"] = args.get("incoming", False)
        args["outgoing"] = True
        if bool(args["incoming"]):
            args["outgoing"] = False

        try:
            if pattern is not None and not pattern.startswith('(?i)'):
                args['pattern'] = '(?i)' + pattern
        except:
            pass

        reg = re.compile('(.*)')
        if not pattern == None:
            try:
                cmd = re.search(reg, pattern)
                try:
                    cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
                except:
                    pass

                try:
                    CMD_LIST[file_test].append(cmd)
                except:
                    CMD_LIST.update({file_test: [cmd]})
            except:
                pass

        if allow_sudo:
            args["from_users"] = list(Var.SUDO_USERS)
            # Mutually exclusive with outgoing (can only set one of either).
            args["incoming"] = True
        del allow_sudo
        try:
            del args["allow_sudo"]
        except:
            pass

        if "allow_edited_updates" in args:
            del args['allow_edited_updates']

        def decorator(func):
            if allow_edited_updates:
                bot.add_event_handler(func, events.MessageEdited(**args))
            bot.add_event_handler(func, events.NewMessage(**args))
            try:
                LOAD_PLUG[file_test].append(func)
            except:
                LOAD_PLUG.update({file_test: [func]})
            return func

        return decorator


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import userbot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Successfully (re)imported "+shortname)
    else:
        import userbot.utils
        import sys
        import importlib
        from pathlib import Path
        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.tgbot = bot.tgbot
        mod.Var = Var
        mod.command = command
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userbot.utils
        mod.Config = Config
        mod.borg = bot
        # support for paperplaneextended
        sys.modules["userbot.events"] = userbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userbot.plugins."+shortname] = mod
        print("Successfully (re)imported "+shortname)

def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except:
            name = f"userbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except:
        raise ValueError

def admin_cmd(**args):
    args["func"] = lambda e: e.via_bot_id is None
    
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(Var.COMMAND_HAND_LER + pattern)
            cmd = Var.COMMAND_HAND_LER + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    # check if the plugin should allow edited updates
    allow_edited_updates = False
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        allow_edited_updates = args["allow_edited_updates"]
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'
    is_message_enabled = True

    return events.NewMessage(**args)

""" Userbot module for managing events.
 One of the main components of the userbot. """

from telethon import events
import asyncio
from userbot import bot
from traceback import format_exc
from time import gmtime, strftime
import math
import subprocess
import sys
import traceback
from datetime import datetime
import time


def register(**args):
    """ Register a new event. """
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', True)

    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = '(?i)' + pattern

    if "disable_edited" in args:
        del args['disable_edited']
    
    reg = re.compile('(.*)')
    if not pattern == None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
        except:
            pass

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception as e:
            LOAD_PLUG.update({file_test: [func]})

        return func

    return decorator


def errors_handler(func):
    async def wrapper(event):
        try:
            return await func(event)
        except Exception:
            pass
    return wrapper

async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for both
    upload.py and download.py"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))

async def is_read(borg, entity, message, is_out=None):
    """
    Returns True if the given message (or id) has been read
    if a id is given, is_out needs to be a bool
    """
    is_out = getattr(message, "out", is_out)
    if not isinstance(is_out, bool):
        raise ValueError(
            "Message was id but is_out not provided or not a bool")
    message_id = getattr(message, "id", message)
    if not isinstance(message_id, int):
        raise ValueError("Failed to extract id from message")

    dialog = (await borg(GetPeerDialogsRequest([entity]))).dialogs[0]
    max_id = dialog.read_outbox_max_id if is_out else dialog.read_inbox_max_id
    return message_id <= max_id

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
    
def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

class Loader():
    def __init__(self, func=None, **args):
        self.Var = Var
        bot.add_event_handler(func, events.NewMessage(**args))

# Not that Great but it will fix sudo reply
async def edit_or_reply(event, user_id, text):
    if user_id in Config.SUDO_USERS:
      reply_to = await event.get_reply_message()
      if reply_to:
        return await reply_to.reply(text)
      else:
        return await event.reply(text)
    else:
        return await event.edit(text)
