// FILE: frontend/src/features/2_SchemeDiscovery/SchemeResults.js
import React from 'react';
import { Heading, VStack, Spinner, Alert, AlertIcon, Text } from '@chakra-ui/react';
import SchemeCard from '../../components/SchemeCard'; // Note the path change

const SchemeResults = ({ isLoading, error, schemes }) => {
  if (isLoading) {
    return (
      <VStack justify="center" py={10}>
        <Spinner size="xl" color="teal.500" />
        <Text>Finding the best schemes for you...</Text>
      </VStack>
    );
  }

  if (error) {
    return (
      <Alert status="error" borderRadius="md">
        <AlertIcon />
        {error}
      </Alert>
    );
  }

  if (schemes.length === 0) {
    // Awaiting user input, show nothing until a search is performed.
    return null;
  }

  return (
    <VStack spacing={6} w="100%" align="stretch">
      <Heading size="lg" textAlign="center">
        We found {schemes.length} matching scheme(s)!
      </Heading>
      {schemes.map((scheme) => (
        <SchemeCard key={scheme.scheme_id} scheme={scheme} />
      ))}
    </VStack>
  );
};

export default SchemeResults;