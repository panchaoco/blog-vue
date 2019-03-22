/**
 *
 */
class MusicPlay {
  /**
   *
   * @param audio
   * @param play_status
   * @param play_url
   */
  constructor(audio = null, play_status = false, play_url = '') {
    this.audio = audio
    this.playStatus = play_status
    this.playUrl = play_url
    this.currentTime = 0
  }

  play() {
    this.audio.play()
  }
  pause() {
    this.audio.pause()
  }
}
