import cookie from './cookie'
global._guid = ''
const _getGuid = () => {
  if (global._guid.length > 0) return global._guid;
  const pgv_pvid = cookie.get("pgv_pvid");
  if (pgv_pvid && pgv_pvid.length > 0) return global._guid = pgv_pvid;
  console.log('pgv_pvid', pgv_pvid)
  const time = (new Date).getUTCMilliseconds();
  return global._guid = Math.round(2147483647 * Math.random()) * time % 1e10,
    document.cookie = "pgv_pvid=" + global._guid + "; Expires=Sun, 18 Jan 2038 00:00:00 GMT; PATH=/;",
    global._guid
}

export default _getGuid
