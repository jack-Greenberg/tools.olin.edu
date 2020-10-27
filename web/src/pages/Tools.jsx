import React from "react";
import { Link } from "react-router-dom";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";

import _ from "lodash";

const toolQuery = gql`
  query {
    tools {
      id
      name
      category {
        name
      }
    }
  }
`

const Tools = () => {
  const { loading, error, data } = useQuery(toolQuery);

  if (loading) {
    return (
      <div>
        Loading...
      </div>
    )
  }

  if (error) {
    // TODO: Implement <Error message={} code={} /> component
  }

  // Sort tools by their category name
  const sorted = _.groupBy(data.tools, "category.name");

  // Create tool lists (multiple ul > li)
  const toolList = Object.keys(sorted).map((category) => {
    const toolItems = sorted[category].map(tool => {
      const shortName = tool.name.toLowerCase();
      return (
        <li data-id={tool.id} key={tool.id}>
          <Link to={"/tools/" + shortName}>{tool.name}</Link>
        </li>
      )
    })

    return (
      <div key={category}>
        <h2>{category}</h2>
        <ul>
          {toolItems}
        </ul>
      </div>
    )
  });

  return (
    <>
      <h1>Tools</h1>
      <p>Click on a tool to visit the page. From there, you can
        start a training.</p>
      {toolList}
    </>
  )
}

export default Tools;
