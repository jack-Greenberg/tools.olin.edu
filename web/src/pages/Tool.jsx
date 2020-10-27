import React from "react";
import { useQuery } from "@apollo/react-hooks";
import gql from "graphql-tag";


const ToolPage = (tool) => {

  const toolQuery = gql`
    query GET_TOOL($tool: String!) {
      tool (
        name: $tool
      ) {
        id
        name
        category {
          name
        }
      }
    }
  `

  const { loading, error, data } = useQuery(toolQuery, {
    variables: { tool }
  });

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

  return (
    <div>

    </div>
  )
}

export default ToolPage;
