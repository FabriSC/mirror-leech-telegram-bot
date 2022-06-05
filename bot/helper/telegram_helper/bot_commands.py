from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start5{CMD_INDEX}'
        self.MirrorCommand = f'mirror5{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror5{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror5{CMD_INDEX}'
        self.CancelMirror = f'cancel5{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall5{CMD_INDEX}'
        self.ListCommand = f'list5{CMD_INDEX}'
        self.SearchCommand = f'search5{CMD_INDEX}'
        self.StatusCommand = f'status5{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users5{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize5{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize5{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo5{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo5{CMD_INDEX}'
        self.PingCommand = f'ping5{CMD_INDEX}'
        self.RestartCommand = f'restart5{CMD_INDEX}'
        self.StatsCommand = f'stats5{CMD_INDEX}'
        self.HelpCommand = f'help5{CMD_INDEX}'
        self.LogCommand = f'log5{CMD_INDEX}'
        self.CloneCommand = f'clone5{CMD_INDEX}'
        self.CountCommand = f'count5{CMD_INDEX}'
        self.WatchCommand = f'watch5{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch5{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror5{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror5{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror5{CMD_INDEX}'
        self.DeleteCommand = f'del5{CMD_INDEX}'
        self.ShellCommand = f'shell5{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp5{CMD_INDEX}'
        self.LeechSetCommand = f'leechset5{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb5{CMD_INDEX}'
        self.LeechCommand = f'leech5{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech5{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech5{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech5{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech5{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech5{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch5{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch5{CMD_INDEX}'
        self.RssListCommand = f'rsslist5{CMD_INDEX}'
        self.RssGetCommand = f'rssget5{CMD_INDEX}'
        self.RssSubCommand = f'rsssub5{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub5{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset5{CMD_INDEX}'
        self.EvalCommand = f'eval5{CMD_INDEX}'
        self.ExecCommand = f'exec5{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals5{CMD_INDEX}'

BotCommands = _BotCommands()
