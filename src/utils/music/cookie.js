import cookieConfig from './config'

export default {
  set: function (e, o, t, c, i) {
    let time = ''
    if (i) {
      time = new Date;
      time.setTime(time.getTime() + 36e5 * i)
    }
    return document.cookie = e + "=" + escape(o) + "; " + (i ? "expires=" + time.toGMTString() + "; " : "") + (c ? "path=" + c + "; " : "path=/; ") + (t ? "domain=" + t + ";" : "domain=" + cookieConfig.DCCookieDomain + ";"), !0
  },
  get: function (serializer) {
    let n, getStr = function (e) {
      if (!e) return e;
      for (; e != unescape(e);) e = unescape(e);
      for (let n = ["<", ">", "'", '"', "%3c", "%3e", "%27", "%22", "%253c", "%253e", "%2527", "%2522"], o = ["&#x3c;", "&#x3e;", "&#x27;", "&#x22;", "%26%23x3c%3B", "%26%23x3e%3B", "%26%23x27%3B", "%26%23x22%3B", "%2526%2523x3c%253B", "%2526%2523x3e%253B", "%2526%2523x27%253B", "%2526%2523x22%253B"], t = 0; t < n.length; t++) e = e.replace(new RegExp(n[t], "gi"), o[t]);
      return e
    };
    return getStr((n = document.cookie.match(RegExp("(^|;\\s*)" + serializer + "=([^;]*)(;|$)"))) ? unescape(n[2]) : "")
  },
  del: function (e, o, t) {
    document.cookie = e + "=; expires=Mon, 26 Jul 1997 05:00:00 GMT; " + (t ? "path=" + t + "; " : "path=/; ") + (o ? "domain=" + o + ";" : "domain=" + cookieConfig.localDomain + ";")
  },
  getACSRFToken: function () {
    function token(str) {
      for (var n = 5381, o = 0, t = str.length; t > o; ++o) n += (n << 5) + str.charCodeAt(o)
      return 2147483647 & n
    }

    return token(this.get("p_skey") || this.get("skey") || this.get("p_lskey") || this.get("lskey"))
  }
};

const commonSetCookie = {
  sck: [],
  sco: {},
  init: function () {
    var e = this.get("pgv_info=", !0);
    if (e != _n) for (var t = e.split("&"), s = 0; s < t.length; s++) {
      var r = t[s].split("=");
      this.set(r[0], unescape(r[1]))
    }
  },
  get: function (e, t) {
    var s, r, a = t ? _d.cookie : this.get("pgv_info=", !0), i = _n;
    if (s = a.indexOf(e), s > -1) {
      if (s += e.length, r = a.indexOf(";", s), -1 == r && (r = a.length), !t) {
        var n = a.indexOf("&", s);
        n > -1 && (r = Math.min(r, n))
      }
      i = a.substring(s, r)
    }
    return i
  },
  set: function (e, t) {
    this.sco[e] = t;
    var s = !1;
    var r = this.sck.length;
    for (var a = 0; r > a; a++) if (e == this.sck[a]) {
      s = !0;
      break
    }
    s || this.sck.push(e)
  },
  setCookie: function (e, t, s) {
    var r = _l.hostname, a = _cookie.get(e + "=", t);
    if (a != _n || s) a = s ? s : a; else {
      switch (e) {
        case"ts_uid":
          _ext.push("nw=1");
          break;
        case"ssid":
          _ch = 1
      }
      a = t ? "" : "s";
      var i = (new Date).getUTCMilliseconds();
      a += Math.round(2147483647 * Math.abs(Math.random() - 1)) * i % 1e10
    }
    if (t) {
      switch (e) {
        case"ts_uid":
          this.saveCookie(e + "=" + a, r, this.getExpires(1051200));
          break;
        case"ts_refer":
          this.saveCookie(e + "=" + a, r, this.getExpires(259200));
          break;
        case"ts_last":
          this.saveCookie(e + "=" + a, r, this.getExpires(30));
          break;
        default:
          this.saveCookie(e + "=" + a, _domainToSet, "expires=Sun, 18 Jan 2038 00:00:00 GMT;")
      }
    } else {
      this.set(e, a)
    }
    return a
  },
  getExpires: function (e) {
    var t = new Date;
    return t.setTime(t.getTime() + 60 * e * 1e3), "expires=" + t.toGMTString()
  },
  save: function () {
    if (_params.sessionSpan) {
      var e = new Date;
      e.setTime(e.getTime() + 60 * _params.sessionSpan * 1e3)
    }
    for (var t = "", s = this.sck.length, r = 0; s > r; r++) t += this.sck[r] + "=" + this.sco[this.sck[r]] + "&";
    t = "pgv_info=" + t.substr(0, t.length - 1);
    var a = "";
    e && (a = "expires=" + e.toGMTString()), this.saveCookie(t, _domainToSet, a)
  },
  saveCookie: function (e, t, s) {
    _d.cookie = e + ";path=/;domain=" + t + ";" + s
  }
}
