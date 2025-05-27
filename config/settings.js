const rootUrl = 'http://192.168.74.1:8000/smart'
// const rootUrl = 'http://192.168.74.1:8000/smart'
// const rootUrl = 'http://192.168.71.100:8000/smart'
// const rootUrl = 'http://0.0.0.0:8000/smart'

// 表示导出---》在任意js中，可以导入--》导入就是这个对象
module.exports = {
  welcome: rootUrl + '/welcome/',
  banner: rootUrl + '/banner/',
  collection: rootUrl + '/collection/',
  area: rootUrl + '/area/',
  statistics: rootUrl + '/statistics/',
  face: rootUrl + '/face/',
  voice:rootUrl + '/voice/',
}