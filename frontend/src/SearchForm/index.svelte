<div class="search-form">
  <input class="search-field" type="text">
  <label class="search-button">
    <!-- https://github.com/ionic-team/ionicons Ionicons, MIT license -->
    <svg xmlns="http://www.w3.org/2000/svg" class="ionicon" viewBox="0 0 512 512"><title>Search</title><path d="M221.09 64a157.09 157.09 0 10157.09 157.09A157.1 157.1 0 00221.09 64z" fill="none" stroke="currentColor" stroke-miterlimit="10" stroke-width="32"/><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-miterlimit="10" stroke-width="32" d="M338.29 338.29L448 448"/></svg>
    <button class="hidden-button">
      Search
    </button>
  </label>
</div>

<style>
  .search-form {
    height: max-content;
    display: inline-grid;
    grid-template-columns: 1fr max-content;
    border: 2px solid rgb(128, 128, 128);
    border-radius: 5px;
    background: white;
    padding: 0.5rem;
    gap: 0.5rem;
  }

  .hidden-button {
    position: absolute;
    height: 0;
    width: 0;
    opacity: 0;
    overflow: hidden;
  }

  .search-field, .search-button {
    font-family: inherit;
    background-color: none;
    border: 0 none;
    height: 2rem;
  }

  .search-field {
    outline: 0 none;
    width: 100%;
    font-size: 2rem;
  }

  .search-button {
    cursor: pointer;
    color: rgb(128, 128, 128);
    padding: 0;
    width: 2rem;
  }
</style>
