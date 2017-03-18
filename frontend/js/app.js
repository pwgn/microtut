
(function() {

    $(".button-collapse").sideNav();

    var apiClient = new MicroApi();

    var mainView = new MainView(document);
    var mainPresenter = new MainPresenter(apiClient, mainView);
    mainPresenter.start();

})();
