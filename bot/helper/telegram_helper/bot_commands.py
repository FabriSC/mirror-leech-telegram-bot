from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start1{CMD_INDEX}'
        self.MirrorCommand = f'mirror1{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror1{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror1{CMD_INDEX}'
        self.CancelMirror = f'cancel1{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall1{CMD_INDEX}'
        self.ListCommand = f'list1{CMD_INDEX}'
        self.SearchCommand = f'search1{CMD_INDEX}'
        self.StatusCommand = f'status1{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users1{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize1{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize1{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo1{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo1{CMD_INDEX}'
        self.PingCommand = f'ping1{CMD_INDEX}'
        self.RestartCommand = f'restart1{CMD_INDEX}'
        self.StatsCommand = f'stats1{CMD_INDEX}'
        self.HelpCommand = f'help1{CMD_INDEX}'
        self.LogCommand = f'log1{CMD_INDEX}'
        self.CloneCommand = f'clone1{CMD_INDEX}'
        self.CountCommand = f'count1{CMD_INDEX}'
        self.WatchCommand = f'watch1{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch1{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror1{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror1{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror1{CMD_INDEX}'
        self.DeleteCommand = f'del1{CMD_INDEX}'
        self.ShellCommand = f'shell1{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp1{CMD_INDEX}'
        self.LeechSetCommand = f'leechset1{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb1{CMD_INDEX}'
        self.LeechCommand = f'leech1{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech1{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech1{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech1{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech1{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech1{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch1{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch1{CMD_INDEX}'
        self.RssListCommand = f'rsslist1{CMD_INDEX}'
        self.RssGetCommand = f'rssget1{CMD_INDEX}'
        self.RssSubCommand = f'rsssub1{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub1{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset1{CMD_INDEX}'
        self.EvalCommand = f'eval1{CMD_INDEX}'
        self.ExecCommand = f'exec1{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals1{CMD_INDEX}'

BotCommands = _BotCommands()
