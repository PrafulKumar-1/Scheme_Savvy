// FILE: frontend/src/pages/FutureFeaturesPage.js

import React from 'react';
import { Box, Heading, Text, VStack, SimpleGrid, Icon, useColorModeValue } from '@chakra-ui/react';
import { TimeIcon} from '@chakra-ui/icons';
import DocumentScanner from '../features/4_DocumentScanner/DocumentScanner';
import Chatbot from '../features/3_Chatbot/Chatbot';
import CommunityForum from '../features/5_Community/CommunityForum';

const FeatureCard = ({ icon, title, children }) => {
  return (
    <VStack
      p={5}
      bg={useColorModeValue('gray.100', 'gray.700')}
      borderRadius="lg"
      align="start"
      spacing={3}
      h="100%"
    >
      <Icon as={icon} w={8} h={8} color="teal.500" />
      <Heading size="md">{title}</Heading>
      <Text color="gray.600">{children}</Text>
    </VStack>
  );
};

const FutureFeaturesPage = () => {
  return (
    <VStack spacing={12}>
      <Box textAlign="center">
        <Heading size="2xl">Our Vision for the Future</Heading>
        <Text fontSize="lg" color="gray.600" mt={2}>
          We are building an ecosystem to provide end-to-end citizen assistance.
        </Text>
      </Box>

      <SimpleGrid columns={{ base: 1, lg: 2 }} spacing={10} w="100%">
        <Chatbot />
        <DocumentScanner />
        <CommunityForum />
         <FeatureCard icon={TimeIcon} title="Lifecycle Alerts">
          Get proactive alerts for application deadlines or when you become eligible for new schemes as your life circumstances change.
        </FeatureCard>
      </SimpleGrid>
    </VStack>
  );
};

export default FutureFeaturesPage;