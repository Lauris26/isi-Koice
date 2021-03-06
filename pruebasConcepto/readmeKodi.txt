None([, username, password])
|
|---Addons
|   |
|   |---ExecuteAddon(addonid[, username, password, params, wait])
|   |       Executes the given addon with the given parameters (if possible)
|   |
|   |---GetAddonDetails(addonid[, username, password, properties])
|   |       Gets the details of a specific addon
|   |
|   |---GetAddons([, username, password, type, content, enabled, properties, limits, installed])
|   |       Gets all available addons
|   |
|   |---SetAddonEnabled(addonid, enabled[, username, password])
|   |       Enables/Disables a specific addon
|
|---Application
|   |
|   |---GetProperties(properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---Quit([, username, password])
|   |       Quit application
|   |
|   |---SetMute(mute[, username, password])
|   |       Toggle mute/unmute
|   |
|   |---SetVolume(volume[, username, password])
|   |       Set the current volume
|
|---AudioLibrary
|   |
|   |---Clean([, username, password, showdialogs])
|   |       Cleans the audio library from non-existent items
|   |
|   |---Export([, username, password, options])
|   |       Exports all items from the audio library
|   |
|   |---GetAlbumDetails(albumid[, username, password, properties])
|   |       Retrieve details about a specific album
|   |
|   |---GetAlbums([, username, password, properties, limits, sort, filter, includesingles, allroles])
|   |       Retrieve all albums from specified artist (and role) or that has songs of the specified genre
|   |
|   |---GetArtistDetails(artistid[, username, password, properties])
|   |       Retrieve details about a specific artist
|   |
|   |---GetArtists([, username, password, albumartistsonly, properties, limits, sort, filter, allroles])
|   |       Retrieve all artists. For backward compatibility by default this implicitly does not include those that only contribute other roles, however absolutely all artists can be returned using allroles=true
|   |
|   |---GetAvailableArt(item[, username, password, arttype])
|   |       Retrieve all potential art URLs for a media item by art type
|   |
|   |---GetAvailableArtTypes(item[, username, password])
|   |       Retrieve a list of potential art types for a media item
|   |
|   |---GetGenres([, username, password, properties, limits, sort])
|   |       Retrieve all genres
|   |
|   |---GetProperties(properties[, username, password])
|   |       Retrieves the values of the music library properties
|   |
|   |---GetRecentlyAddedAlbums([, username, password, properties, limits, sort])
|   |       Retrieve recently added albums
|   |
|   |---GetRecentlyAddedSongs([, username, password, albumlimit, properties, limits, sort])
|   |       Retrieve recently added songs
|   |
|   |---GetRecentlyPlayedAlbums([, username, password, properties, limits, sort])
|   |       Retrieve recently played albums
|   |
|   |---GetRecentlyPlayedSongs([, username, password, properties, limits, sort])
|   |       Retrieve recently played songs
|   |
|   |---GetRoles([, username, password, properties, limits, sort])
|   |       Retrieve all contributor roles
|   |
|   |---GetSongDetails(songid[, username, password, properties])
|   |       Retrieve details about a specific song
|   |
|   |---GetSongs([, username, password, properties, limits, sort, filter, includesingles, allroles, singlesonly])
|   |       Retrieve all songs from specified album, artist or genre
|   |
|   |---GetSources([, username, password, properties, limits, sort])
|   |       Get all music sources, including unique ID
|   |
|   |---Scan([, username, password, directory, showdialogs])
|   |       Scans the audio sources for new library items
|   |
|   |---SetAlbumDetails(albumid[, username, password, title, artist, description, genre, theme, mood, style, type, albumlabel, rating, year, userrating, votes, musicbrainzalbumid, musicbrainzreleasegroupid, sortartist, displayartist, musicbrainzalbumartistid, art, isboxset, releasedate, originaldate])
|   |       Update the given album with the given details
|   |
|   |---SetArtistDetails(artistid[, username, password, artist, instrument, style, mood, born, formed, description, genre, died, disbanded, yearsactive, musicbrainzartistid, sortname, type, gender, disambiguation, art])
|   |       Update the given artist with the given details
|   |
|   |---SetSongDetails(songid[, username, password, title, artist, genre, year, rating, track, disc, duration, comment, musicbrainztrackid, musicbrainzartistid, playcount, lastplayed, userrating, votes, displayartist, sortartist, mood, art, disctitle, releasedate, originaldate, bpm])
|   |       Update the given song with the given details
|
|---Favourites
|   |
|   |---AddFavourite(title, type[, username, password, path, window, windowparameter, thumbnail])
|   |       Add a favourite with the given details
|   |
|   |---GetFavourites([, username, password, type, properties])
|   |       Retrieve all favourites
|
|---Files
|   |
|   |---GetDirectory(directory[, username, password, media, properties, sort, limits])
|   |       Get the directories and files in the given directory
|   |
|   |---GetFileDetails(file[, username, password, media, properties])
|   |       Get details for a specific file
|   |
|   |---GetSources(media[, username, password, limits, sort])
|   |       Get the sources of the media windows
|   |
|   |---PrepareDownload(path[, username, password])
|   |       Provides a way to download a given file (e.g. providing an URL to the real file location)
|   |
|   |---SetFileDetails(file, media[, username, password, playcount, lastplayed, resume])
|   |       Update the given specific file with the given details
|
|---GUI
|   |
|   |---ActivateWindow(window[, username, password, parameters])
|   |       Activates the given window
|   |
|   |---GetProperties(properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---GetStereoscopicModes([, username, password])
|   |       Returns the supported stereoscopic modes of the GUI
|   |
|   |---SetFullscreen(fullscreen[, username, password])
|   |       Toggle fullscreen/GUI
|   |
|   |---SetStereoscopicMode(mode[, username, password])
|   |       Sets the stereoscopic mode of the GUI to the given mode
|   |
|   |---ShowNotification(title, message[, username, password, image, displaytime])
|   |       Shows a GUI notification
|
|---Input
|   |
|   |---Back([, username, password])
|   |       Goes back in GUI
|   |
|   |---ButtonEvent(button, keymap[, username, password, holdtime])
|   |       Send a button press event
|   |
|   |---ContextMenu([, username, password])
|   |       Shows the context menu
|   |
|   |---Down([, username, password])
|   |       Navigate down in GUI
|   |
|   |---ExecuteAction(action[, username, password])
|   |       Execute a specific action
|   |
|   |---Home([, username, password])
|   |       Goes to home window in GUI
|   |
|   |---Info([, username, password])
|   |       Shows the information dialog
|   |
|   |---Left([, username, password])
|   |       Navigate left in GUI
|   |
|   |---Right([, username, password])
|   |       Navigate right in GUI
|   |
|   |---Select([, username, password])
|   |       Select current item in GUI
|   |
|   |---SendText(text[, username, password, done])
|   |       Send a generic (unicode) text
|   |
|   |---ShowCodec([, username, password])
|   |       Show codec information of the playing item
|   |
|   |---ShowOSD([, username, password])
|   |       Show the on-screen display for the current player
|   |
|   |---ShowPlayerProcessInfo([, username, password])
|   |       Show player process information of the playing item, like video decoder, pixel format, pvr signal strength, ...
|   |
|   |---Up([, username, password])
|   |       Navigate up in GUI
|
|---JSONRPC
|   |
|   |---Introspect([, username, password, getdescriptions, getmetadata, filterbytransport, filter])
|   |       Enumerates all actions and descriptions
|   |
|   |---NotifyAll(sender, message[, username, password, data])
|   |       Notify all other connected clients
|   |
|   |---Permission([, username, password])
|   |       Retrieve the clients permissions
|   |
|   |---Ping([, username, password])
|   |       Ping responder
|   |
|   |---Version([, username, password])
|   |       Retrieve the JSON-RPC protocol version.
|
|---PVR
|   |
|   |---AddTimer(broadcastid[, username, password, timerrule, reminder])
|   |       Adds a timer to record the given show one times or a timer rule to record all showings of the given show or adds a reminder timer or reminder timer rule
|   |
|   |---DeleteTimer(timerid[, username, password])
|   |       Deletes a onetime timer or a timer rule
|   |
|   |---GetBroadcastDetails(broadcastid[, username, password, properties])
|   |       Retrieves the details of a specific broadcast
|   |
|   |---GetBroadcastIsPlayable(broadcastid[, username, password])
|   |       Retrieves whether or not a broadcast is playable
|   |
|   |---GetBroadcasts(channelid[, username, password, properties, limits])
|   |       Retrieves the program of a specific channel
|   |
|   |---GetChannelDetails(channelid[, username, password, properties])
|   |       Retrieves the details of a specific channel
|   |
|   |---GetChannelGroupDetails(channelgroupid[, username, password, channels])
|   |       Retrieves the details of a specific channel group
|   |
|   |---GetChannelGroups(channeltype[, username, password, limits])
|   |       Retrieves the channel groups for the specified type
|   |
|   |---GetChannels(channelgroupid[, username, password, properties, limits, sort])
|   |       Retrieves the channel list
|   |
|   |---GetClients([, username, password, limits])
|   |       Retrieves the enabled PVR clients and their capabilities
|   |
|   |---GetProperties(properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---GetRecordingDetails(recordingid[, username, password, properties])
|   |       Retrieves the details of a specific recording
|   |
|   |---GetRecordings([, username, password, properties, limits, sort])
|   |       Retrieves the recordings
|   |
|   |---GetTimerDetails(timerid[, username, password, properties])
|   |       Retrieves the details of a specific timer
|   |
|   |---GetTimers([, username, password, properties, limits, sort])
|   |       Retrieves the timers
|   |
|   |---Record([, username, password, record, channel])
|   |       Toggle recording of a channel
|   |
|   |---Scan([, username, password, clientid])
|   |       Starts a channel scan
|   |
|   |---ToggleTimer(broadcastid[, username, password, timerrule])
|   |       Creates or deletes a onetime timer or timer rule for a given show. If it exists, it will be deleted. If it does not exist, it will be created
|
|---Player
|   |
|   |---AddSubtitle(playerid, subtitle[, username, password])
|   |       Add subtitle to the player
|   |
|   |---GetActivePlayers([, username, password])
|   |       Returns all active players
|   |
|   |---GetItem(playerid[, username, password, properties])
|   |       Retrieves the currently played item
|   |
|   |---GetPlayers([, username, password, media])
|   |       Get a list of available players
|   |
|   |---GetProperties(playerid, properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---GetViewMode([, username, password])
|   |       Get view mode of video player
|   |
|   |---GoTo(playerid, to[, username, password])
|   |       Go to previous/next/specific item in the playlist
|   |
|   |---Move(playerid, direction[, username, password])
|   |       If picture is zoomed move viewport left/right/up/down otherwise skip previous/next
|   |
|   |---Open([, username, password, item, options])
|   |       Start playback of either the playlist with the given ID, a slideshow with the pictures from the given directory or a single file or an item from the database.
|   |
|   |---PlayPause(playerid[, username, password, play])
|   |       Pauses or unpause playback and returns the new state
|   |
|   |---Rotate(playerid[, username, password, value])
|   |       Rotates current picture
|   |
|   |---Seek(playerid, value[, username, password])
|   |       Seek through the playing item
|   |
|   |---SetAudioStream(playerid, stream[, username, password])
|   |       Set the audio stream played by the player
|   |
|   |---SetPartymode(playerid, partymode[, username, password])
|   |       Turn partymode on or off
|   |
|   |---SetRepeat(playerid, repeat[, username, password])
|   |       Set the repeat mode of the player
|   |
|   |---SetShuffle(playerid, shuffle[, username, password])
|   |       Shuffle/Unshuffle items in the player
|   |
|   |---SetSpeed(playerid, speed[, username, password])
|   |       Set the speed of the current playback
|   |
|   |---SetSubtitle(playerid, subtitle[, username, password, enable])
|   |       Set the subtitle displayed by the player
|   |
|   |---SetVideoStream(playerid, stream[, username, password])
|   |       Set the video stream played by the player
|   |
|   |---SetViewMode(viewmode[, username, password])
|   |       Set view mode of video player
|   |
|   |---Stop(playerid[, username, password])
|   |       Stops playback
|   |
|   |---Zoom(playerid, zoom[, username, password])
|   |       Zoom current picture
|
|---Playlist
|   |
|   |---Add(playlistid, item[, username, password])
|   |       Add item(s) to playlist
|   |
|   |---Clear(playlistid[, username, password])
|   |       Clear playlist
|   |
|   |---GetItems(playlistid[, username, password, properties, limits, sort])
|   |       Get all items from playlist
|   |
|   |---GetPlaylists([, username, password])
|   |       Returns all existing playlists
|   |
|   |---GetProperties(playlistid, properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---Insert(playlistid, position, item[, username, password])
|   |       Insert item(s) into playlist. Does not work for picture playlists (aka slideshows).
|   |
|   |---Remove(playlistid, position[, username, password])
|   |       Remove item from playlist. Does not work for picture playlists (aka slideshows).
|   |
|   |---Swap(playlistid, position1, position2[, username, password])
|   |       Swap items in the playlist. Does not work for picture playlists (aka slideshows).
|
|---Profiles
|   |
|   |---GetCurrentProfile([, username, password, properties])
|   |       Retrieve the current profile
|   |
|   |---GetProfiles([, username, password, properties, limits, sort])
|   |       Retrieve all profiles
|   |
|   |---LoadProfile(profile[, username, password, prompt])
|   |       Load the specified profile
|
|---Settings
|   |
|   |---GetCategories([, username, password, level, section, properties])
|   |       Retrieves all setting categories
|   |
|   |---GetSections([, username, password, level, properties])
|   |       Retrieves all setting sections
|   |
|   |---GetSettingValue(setting[, username, password])
|   |       Retrieves the value of a setting
|   |
|   |---GetSettings([, username, password, level, filter])
|   |       Retrieves all settings
|   |
|   |---ResetSettingValue(setting[, username, password])
|   |       Resets the value of a setting
|   |
|   |---SetSettingValue(setting, value[, username, password])
|   |       Changes the value of a setting
|
|---System
|   |
|   |---EjectOpticalDrive([, username, password])
|   |       Ejects or closes the optical disc drive (if available)
|   |
|   |---GetProperties(properties[, username, password])
|   |       Retrieves the values of the given properties
|   |
|   |---Hibernate([, username, password])
|   |       Puts the system running Kodi into hibernate mode
|   |
|   |---Reboot([, username, password])
|   |       Reboots the system running Kodi
|   |
|   |---Shutdown([, username, password])
|   |       Shuts the system running Kodi down
|   |
|   |---Suspend([, username, password])
|   |       Suspends the system running Kodi
|
|---Textures
|   |
|   |---GetTextures([, username, password, properties, filter])
|   |       Retrieve all textures
|   |
|   |---RemoveTexture(textureid[, username, password])
|   |       Remove the specified texture
|
|---VideoLibrary
|   |
|   |---Clean([, username, password, showdialogs, content, directory])
|   |       Cleans the video library for non-existent items
|   |
|   |---Export([, username, password, options])
|   |       Exports all items from the video library
|   |
|   |---GetAvailableArt(item[, username, password, arttype])
|   |       Retrieve all potential art URLs for a media item by art type
|   |
|   |---GetAvailableArtTypes(item[, username, password])
|   |       Retrieve a list of potential art types for a media item
|   |
|   |---GetEpisodeDetails(episodeid[, username, password, properties])
|   |       Retrieve details about a specific tv show episode
|   |
|   |---GetEpisodes([, username, password, tvshowid, season, properties, limits, sort, filter])
|   |       Retrieve all tv show episodes
|   |
|   |---GetGenres(type[, username, password, properties, limits, sort])
|   |       Retrieve all genres
|   |
|   |---GetInProgressTVShows([, username, password, properties, limits, sort])
|   |       Retrieve all in progress tvshows
|   |
|   |---GetMovieDetails(movieid[, username, password, properties])
|   |       Retrieve details about a specific movie
|   |
|   |---GetMovieSetDetails(setid[, username, password, properties, movies])
|   |       Retrieve details about a specific movie set
|   |
|   |---GetMovieSets([, username, password, properties, limits, sort])
|   |       Retrieve all movie sets
|   |
|   |---GetMovies([, username, password, properties, limits, sort, filter])
|   |       Retrieve all movies
|   |
|   |---GetMusicVideoDetails(musicvideoid[, username, password, properties])
|   |       Retrieve details about a specific music video
|   |
|   |---GetMusicVideos([, username, password, properties, limits, sort, filter])
|   |       Retrieve all music videos
|   |
|   |---GetRecentlyAddedEpisodes([, username, password, properties, limits, sort])
|   |       Retrieve all recently added tv episodes
|   |
|   |---GetRecentlyAddedMovies([, username, password, properties, limits, sort])
|   |       Retrieve all recently added movies
|   |
|   |---GetRecentlyAddedMusicVideos([, username, password, properties, limits, sort])
|   |       Retrieve all recently added music videos
|   |
|   |---GetSeasonDetails(seasonid[, username, password, properties])
|   |       Retrieve details about a specific tv show season
|   |
|   |---GetSeasons([, username, password, tvshowid, properties, limits, sort])
|   |       Retrieve all tv seasons
|   |
|   |---GetTVShowDetails(tvshowid[, username, password, properties])
|   |       Retrieve details about a specific tv show
|   |
|   |---GetTVShows([, username, password, properties, limits, sort, filter])
|   |       Retrieve all tv shows
|   |
|   |---GetTags(type[, username, password, properties, limits, sort])
|   |       Retrieve all tags
|   |
|   |---RefreshEpisode(episodeid[, username, password, ignorenfo, title])
|   |       Refresh the given episode in the library
|   |
|   |---RefreshMovie(movieid[, username, password, ignorenfo, title])
|   |       Refresh the given movie in the library
|   |
|   |---RefreshMusicVideo(musicvideoid[, username, password, ignorenfo, title])
|   |       Refresh the given music video in the library
|   |
|   |---RefreshTVShow(tvshowid[, username, password, ignorenfo, refreshepisodes, title])
|   |       Refresh the given tv show in the library
|   |
|   |---RemoveEpisode(episodeid[, username, password])
|   |       Removes the given episode from the library
|   |
|   |---RemoveMovie(movieid[, username, password])
|   |       Removes the given movie from the library
|   |
|   |---RemoveMusicVideo(musicvideoid[, username, password])
|   |       Removes the given music video from the library
|   |
|   |---RemoveTVShow(tvshowid[, username, password])
|   |       Removes the given tv show from the library
|   |
|   |---Scan([, username, password, directory, showdialogs])
|   |       Scans the video sources for new library items
|   |
|   |---SetEpisodeDetails(episodeid[, username, password, title, playcount, runtime, director, plot, rating, votes, lastplayed, writer, firstaired, productioncode, season, episode, originaltitle, thumbnail, fanart, art, resume, userrating, ratings, dateadded, uniqueid])
|   |       Update the given episode with the given details
|   |
|   |---SetMovieDetails(movieid[, username, password, title, playcount, runtime, director, studio, year, plot, genre, rating, mpaa, imdbnumber, votes, lastplayed, originaltitle, trailer, tagline, plotoutline, writer, country, top250, sorttitle, set, showlink, thumbnail, fanart, tag, art, resume, userrating, ratings, dateadded, premiered, uniqueid])
|   |       Update the given movie with the given details
|   |
|   |---SetMovieSetDetails(setid[, username, password, title, art, plot])
|   |       Update the given movie set with the given details
|   |
|   |---SetMusicVideoDetails(musicvideoid[, username, password, title, playcount, runtime, director, studio, year, plot, album, artist, genre, track, lastplayed, thumbnail, fanart, tag, art, resume, rating, userrating, dateadded, premiered])
|   |       Update the given music video with the given details
|   |
|   |---SetSeasonDetails(seasonid[, username, password, art, userrating, title])
|   |       Update the given season with the given details
|   |
|   |---SetTVShowDetails(tvshowid[, username, password, title, playcount, studio, plot, genre, rating, mpaa, imdbnumber, premiered, votes, lastplayed, originaltitle, sorttitle, episodeguide, thumbnail, fanart, tag, art, userrating, ratings, dateadded, runtime, status, uniqueid])
|   |       Update the given tvshow with the given details
|
|---XBMC
|   |
|   |---GetInfoBooleans(booleans[, username, password])
|   |       Retrieve info booleans about Kodi and the system
|   |
|   |---GetInfoLabels(labels[, username, password])
|   |       Retrieve info labels about Kodi and the system
