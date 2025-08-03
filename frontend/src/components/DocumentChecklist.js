// FILE: frontend/src/components/DocumentChecklist.js

import React from 'react';
import { List, ListItem, ListIcon, Heading, VStack } from '@chakra-ui/react';
import { CheckCircleIcon } from '@chakra-ui/icons';

const DocumentChecklist = ({ documents }) => {
  if (!documents || documents.length === 0) {
    return null;
  }

  return (
    <VStack align="start" spacing={2} w="100%">
      <Heading size="sm" color="gray.800">Required Documents:</Heading>
      <List spacing={2}>
        {documents.map((doc, index) => (
          <ListItem key={index} color="gray.700">
            <ListIcon as={CheckCircleIcon} color="green.500" />
            {doc}
          </ListItem>
        ))}
      </List>
    </VStack>
  );
};

// This is the line that was missing
export default DocumentChecklist;