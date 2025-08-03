// FILE: frontend/src/pages/HomePage.js
// This page now contains the main feature: profiling and results.
import React, { useState } from 'react';
import { Box, Heading, Text, VStack } from '@chakra-ui/react';
import ProfilingForm from '../features/1_Profiling/ProfilingForm';
import SchemeResults from '../features/2_SchemeDiscovery/SchemeResults';

const HomePage = () => {
  const [schemes, setSchemes] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  return (
    <VStack spacing={10} align="stretch">
      <Box textAlign="center">
        <Heading as="h1" size="2xl" bgGradient="linear(to-r, teal.500, green.500)" bgClip="text">
          SchemeSavvy
        </Heading>
        <Text fontSize="lg" color="gray.600" mt={2}>
          Your personal guide to government schemes. Answer a few questions to unlock your benefits.
        </Text>
      </Box>

      <ProfilingForm
        setIsLoading={setIsLoading}
        setError={setError}
        setSchemes={setSchemes}
      />

      <SchemeResults
        isLoading={isLoading}
        error={error}
        schemes={schemes}
      />
    </VStack>
  );
};

export default HomePage;