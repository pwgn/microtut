
(function() {

    $(".button-collapse").sideNav();

    var mainView = new MainView(document);
    var mainPresenter = new MainPresenter(mainView);
    mainPresenter.start();

})();
