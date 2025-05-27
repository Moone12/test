Page({
  /**
   * 页面的初始数据
   */
  data: {
    activityList: [
      {
        id: 1,
        name: "社区运动会",
        time: "2025年6月1日 9:00 - 12:00",
        location: "社区广场",
        imageUrl: "/images/activity/OIP-C.jpg"
      },
      {
        id: 2,
        name: "亲子手工活动",
        time: "2025年6月8日 14:00 - 16:00",
        location: "社区活动中心",
        imageUrl: "/images/activity/OIP-C.jpg"
      },
      {
        id: 3,
        name: "环保志愿者活动",
        time: "2025年6月15日 8:30 - 11:30",
        location: "社区公园",
        imageUrl: "/images/activity/OIP-C.jpg"
      }
    ],
    activity: {} // 添加activity数据字段
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    console.log('页面加载完成');
    // 这里可以处理从详情页返回的数据
  },

  /**
   * 跳转到活动详情页
   */
  goToDetail(e) {
    const activityId = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/activityDetail/activityDetail?id=${activityId}`
    });
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {
    console.log('页面初次渲染完成');
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {
    console.log('页面显示');
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {
    console.log('页面隐藏');
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {
    console.log('页面卸载');
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {
    console.log('用户下拉刷新');
    // 这里可以实现下拉刷新逻辑
    // 刷新完成后调用 wx.stopPullDownRefresh() 停止下拉刷新动画
    setTimeout(() => {
      wx.stopPullDownRefresh();
    }, 1000);
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {
    console.log('页面上拉触底');
    // 这里可以实现加载更多数据的逻辑
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {
    return {
      title: '社区活动',
      path: '/pages/activity/activity',
      success: function(res) {
        console.log('分享成功');
      },
      fail: function(res) {
        console.log('分享失败');
      }
    }
  }
})