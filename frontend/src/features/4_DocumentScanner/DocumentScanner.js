// Placeholder UI for the OCR feature.

import React from 'react';
import { Box, VStack, Icon, Heading, Text, Button } from '@chakra-ui/react';
import { ViewIcon } from '@chakra-ui/icons';

const DocumentScanner = () => {
  return (
    <VStack
      h="300px"
      w="100%"
      borderWidth={1}
      borderRadius="lg"
      boxShadow="lg"
      bg="gray.50"
      p={8}
      spacing={4}
      justify="center"
      borderStyle="dashed"
    >
      <Icon as={ViewIcon} w={16} h={16} color="gray.400" />
      <Heading size="md">Profile via Document Scan</Heading>
      <Text color="gray.600">
        Soon, you'll be able to scan your Aadhaar card to create your profile instantly.
      </Text>
      <Button colorScheme="teal" isDisabled>
        Open Camera
      </Button>
    </VStack>
  );
};

export default DocumentScanner;