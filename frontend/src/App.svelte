<script lang="ts">
  import SearchForm from '@/SearchForm/index.svelte';
</script>

<div class="App centralized">
  <SearchForm />
</div>

<style>
  :global(html, body) {
    height: 100%;
    margin: 0;
    padding: 0;
  }

  :global(body) {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 18px;
    line-height: 1.5;
    background-color: rgb(240, 240, 240);
  }

  .App {
    height: 100%;
    display: grid;
    box-sizing: border-box;
    align-items: center;
    padding: 1rem;
  }

  .App.centralized {
    max-width: 800px;
    margin: 0 auto;
  }
</style>

