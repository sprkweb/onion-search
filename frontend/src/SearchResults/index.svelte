<script lang="ts">
  import { query } from '@/stores'

  const apiUrl = 'https://qcsxorzpfj.execute-api.eu-central-1.amazonaws.com/goognion-api-prototype'

  let results: Array<{
      _id: string,
      fields: { title: string[], description: string[] }
    }>
  function updateResults(q: string) {
    if (q.trim() != '')
      fetch(apiUrl + '?q=' + q)
        .then(r => r.json())
        .then(r => results = r.hits?.hits)
  }

  query.subscribe(value => {
    updateResults(value)
  })
</script>

{#if results}
  <div class="results">
    {#each results as page}
      {#if page && page.fields}
        <article class="page-card">
          <header>
            <h2 class="page-card-title">
              <a href={page._id} rel="noreferrer">{ page.fields.title ? page.fields.title[0] : page._id }</a>
            </h2>
            <a href={page._id} rel="noreferrer" class="page-card-link">{page._id}</a>
          </header>
          {#if page.fields.description}
            <p class="page-card-description">
              <a href={page._id} rel="noreferrer">{ page.fields.description[0] }</a>
            </p>
          {/if}
        </article>
      {/if}
    {/each}
  </div>
{/if}

<style>
  .results {
    min-height: 0;
    max-height: 100%;
    overflow-wrap: break-word;
    overflow-y: scroll;
  }

  .page-card {
    margin-bottom: 2rem;
  }

  .page-card-title {
    margin: 0;
    color: darkblue;
    font-weight: inherit;
  }

  .page-card-link {
    color: grey;
  }

  p {
    margin: 0;
  }

  a {
    color: inherit;
    text-decoration: none;
  }
</style>
